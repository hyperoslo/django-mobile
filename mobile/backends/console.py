"""
SMS backend that writes messages to console instead of sending them.
"""
import sys
import threading

from mobile.backends.base import BaseBackend


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
                stream.write('Message: %s\n'   % message)
                stream.write('---------------------------------\n')
                stream.flush()  # flush after each message
            except:
                pass

            return [1, 'Message was successfully written to console']

        @classmethod
        def receive(self, data):
            """Return IncomingSMS instance from parsed data."""
            raise NotImplementedError
            
    class MMS:
        
        @classmethod
        def receive(self, data):
            """Return IncomingMMS instance from parsed data."""
            raise NotImplementedError
