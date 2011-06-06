# encoding: utf-8

from httplib import HTTPConnection
from base64 import b64encode, b64decode
from xml.etree import ElementTree
import re

from django.core.files.base import ContentFile

from mobile.settings import GATE_USERNAME, GATE_PASSWORD
import mobile.models
        
class GateBackend:
    """Aspiro Gate Backend."""
    
    class SMS:
    
        @classmethod
        def send(self, recipient, sender, price, country, message):
            """
            Send an SMS and return its initial delivery status code.
        
            Delivery status codes:
            201 -- Message is received and is being processed.
            202 -- Message is aknowledged by operator and is being processed.
            203 -- Message is billed and delivered.
            204 -- Message is billed.
            299 -- Temporary undefined status. Message is being processed.
            901 -- Customer has too low credit, the message cannot be delivered.
            902 -- The message expired and could not be delivered.
            903 -- The customers number is temporarily barred.
            904 -- The phone number is permanently barred.
            905 -- The number is barred from overcharged messages.
            906 -- The correct operator for phone number could not be found and the message could not be delivered.
            907 -- The message is billed and the operator confirms billing, but an error occurred when trying to deliver the message.
            909 -- There was a problem with the message format, operator rejected the message.
            910 -- Customer is too young to receive this content.
            911 -- The customer's operator was not correct, trying to resend the message to the correct operator.
            912 -- User balance has been reached for the shortcode, and operator denies more overcharged messages.
            913 -- Service rejected by the user.
            951 -- User is blacklisted due to request from Operator or User. Message cannot be sent to user.
            999 -- General error. Covers all errors not specified with a unique error code.
        
            See Gate API Documentation: http://merlin.aspiro.com/avalon-doc/api/gate-api.pdf
        
            """
        
            headers = {
                'Authorization': 'Basic %s' % b64encode(
                    '%s:%s' % (GATE_USERNAME, GATE_PASSWORD)
                )
            }
        
            body  = u'<?xml version="1.0" encoding="UTF-8" ?>'
            body += u'<gate>'
            body += u'   <targetNumber>%s</targetNumber>' % recipient
            body += u'   <accessNumber>%s</accessNumber>' % sender
            body += u'   <country>%s</country>' % country
            body += u'   <price>%s</price>' % price
            body += u'   <sms>'
            body += u'       <content><![CDATA[%s]]></content>' % message
            body += u'   </sms>'
            body += u'</gate>'

            connection = HTTPConnection('www.mobile-entry.com', timeout=10)
            connection.request('POST', '/gate/service', body.encode('utf-8'), headers)
            response = connection.getresponse()
            body = response.read()
        
            try:
                xml = ElementTree.XML(body)
                return xml.find('status').text
            except:
                raise StandardError('API response malformed')
        
        @classmethod
        def receive(self, data):
            """Return IncomingSMS instance from parsed data."""
            try:
                xml = ElementTree.XML(data)
            except:
                raise StandardError("API request malformed")
                
            sms = mobile.models.IncomingSMS(
                id = xml.find('id').text,
                country = xml.find('country').text,
                sender = xml.find('senderNumber').text,
                recipient = xml.find('targetNumber').text,
                message = xml.find('sms/content').text,
                source = data
            )
            
            if xml.find('keyconfig'):
                sms.keyword = xml.find('keyconfig/keyword').text
                sms.message = re.sub(
                    pattern = re.compile(sms.keyword, flags=re.IGNORECASE | re.UNICODE),
                    repl = '',
                    string = sms.message
                )
                
            return sms.save()
            
    class MMS:
        
        @classmethod
        def receive(self, data):
            """Return IncomingMMS instance from parsed data."""
            try:
                xml = ElementTree.XML(data)
            except:
                raise StandardError("API request malformed")
                
            mms = mobile.models.IncomingMMS.objects.create(
                id = xml.find('id').text,
                country = xml.find('country').text,
                sender = xml.find('senderNumber').text,
                recipient = xml.find('targetNumber').text,
                subject = xml.find('mms/subject').text,
                source = data
            )
            
            for item in xml.findall('mms/item'):
                if item.find('base64').text == 'true':
                    data = b64decode(item.find('content').text)
                else:
                    data = item.find('content').text
                
                mms_file = mobile.models.MMSFile(
                    mms = mms
                )
                
                # Extract content type from MIME data
                matches = re.search('([^;]*/[^;]*);', item.find('mimeType').text)
                if matches:
                    mms_file.content_type = matches.group(1)
                
                # Save file
                mms_file.file.save(
                    name = item.find('name').text,
                    content = ContentFile(data)
                )
                
                mms_file.save()

            return mms