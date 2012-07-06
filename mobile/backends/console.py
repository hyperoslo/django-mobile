"""
SMS backend that writes messages to console instead of sending them.
"""
import re
import sys
import threading

from django.http import QueryDict

from mobile.backends.base import BaseBackend
import mobile.models


class Backend(BaseBackend):

    class SMS:
        
        @classmethod
        def send(self, recipient, sender, price, country, message, **kwargs):
            """Write message to the stream in a thread-safe way."""

            stream = kwargs.pop('stream', sys.stdout)

            try:
                stream.write('SMS -----------------------------\n')
                stream.write('Recipient: %s\n' % recipient)
                stream.write('Sender: %s\n'    % sender)
                stream.write('Country: %s\n'   % country)
                stream.write('Price: %s\n'     % price)
                stream.write('Message: %s\n'   % message.encode('utf-8'))
                stream.write('---------------------------------\n')
                stream.flush()  # flush after each message
            except:
                pass

            return [1, 'Message was successfully written to console']

        @classmethod
        def receive(self, data):
            """Return IncomingSMS instance from parsed data."""
            
            data = QueryDict(data).copy()
            
            sms = mobile.models.IncomingSMS(
                sender = data.get('sender'),
                recipient = data.get('recipient'),
                message = data.get('message'),
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
