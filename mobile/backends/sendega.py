# encoding: utf-8


import os
import logging
import suds
from suds.client import Client

from django.utils.encoding import force_unicode, smart_unicode
from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse, QueryDict
from django.template import loader
from django.template import Context
from django.template import Template

#from httplib import HTTPConnection
#from base64 import b64encode, b64decode
#from xml.etree import ElementTree
import re

#from django.core.files.base import ContentFile

from mobile.backends.base import BaseBackend
from mobile.settings import GATE_USERNAME, GATE_PASSWORD
import mobile.models


GATEWAY_URL = "https://smsc.sendega.com/Content.asmx?WSDL"

logging.basicConfig(level=logging.CRITICAL)
logging.getLogger('suds.client').setLevel(logging.CRITICAL)
logging.getLogger('suds.transport').setLevel(logging.CRITICAL)
logging.getLogger('suds.wsdl').setLevel(logging.CRITICAL)
logging.getLogger('suds.xsd.schema').setLevel(logging.CRITICAL)
        
class Backend(BaseBackend):
    """Sendega Gate Backend."""
    
    class SMS:
    
        @classmethod
        def send(self, recipient, sender, price, country, message):
            """
            Send an SMS and return its initial delivery status code.
        
            Delivery status codes:
            0 -- Message is received and is being processed.
            1001 -- Not validated
            1003 -- Wrong format: pid/dcs
            1004 -- Erroneous typeid
            1020 -- Fromalpha too long
            1021 -- Fromnumber too long
            1022 -- Erroneous recipient, integer overflow
            1023 -- No message content submitted
            1024 -- Premium sms must have abbreviated number as sender
            1025 -- The message sender is not allowed
            1026 -- Balance to low
            1027 -- Message too long
            1028 -- Alphanumeric sender is not valid
            1099 -- Internal error
            9001 -- Username and password does not match
            9002 -- Account is closed
            9004 -- Http not enabled
            9005 -- Smpp not enabled
            9006 -- Ip not allowed
            9007 -- Demo account empty
        
            See Gate API Documentation: http://www.sendega.no/downloads/Sendega%20API%20documentation%20v2.0.pdf
        
            """
        
            client = Client(GATEWAY_URL)
            client.set_options(port='ContentSoap')
        
            result = client.service.Send(
                username = GATE_USERNAME, 
                password = GATE_PASSWORD, 
                sender = sender, 
                destination = recipient, 
                pricegroup = price, 
                contentTypeID = 1, 
                contentHeader = "", 
                content = message, 
                dlrUrl = "http://myserver.example/mydlrUrl/", 
                ageLimit = 0, 
                extID = "", 
                sendDate = "", 
                refID = "", 
                priority = 0, 
                gwID = 0, 
                pid = 0, 
                dcs = 0
            )
        
            if result.Success:
                return [result.ErrorNumber, 'Message is received and is being processed.']
            else:
                return [result.ErrorNumber, result.ErrorMessage]
        
        @classmethod
        def receive(self, data):
            """Return IncomingSMS instance from parsed data."""
            
            data = QueryDict(data).copy()
            
            sms = mobile.models.IncomingSMS(
                message_id = data.get('msgid'),
                country = data.get('mcc'),
                sender = data.get('msisdn'),
                recipient = data.get('shortcode'),
                message = data.get('msg'),
                source = data
            )

            try:
                sms.keyword = data.get('keyword')
                sms.message = re.sub(
                    pattern = re.compile(sms.keyword + " ", flags=re.IGNORECASE | re.UNICODE),
                    repl = '',
                    string = sms.message
                )
            except:
                pass
            
            return sms.save()
            
    class MMS:
        
        @classmethod
        def receive(self, data):
            """Return IncomingMMS instance from parsed data."""
            raise NotImplementedError
