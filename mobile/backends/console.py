"""
SMS backend that writes messages to console instead of sending them.
"""
import sys
import threading

from mobile.backends.base import BaseBackend


class Backend(BaseBackend):

    class SMS:
        
        @classmethod
        def send(self, recipient, sender, price, country, message):
            """Write message to the stream in a thread-safe way."""

            stream = kwargs.pop('stream', sys.stdout)

            try:
                self.stream.write('SMS ----------------------------')
                self.stream.write('Recipient: %s' % recipient)
                self.stream.write('Sender: %s' % sender)
                self.stream.write('Country: %s' % country)
                self.stream.write('Price: %s' % price)
                self.stream.write('Message: %s' % message)
                self.stream.write('---------------------------------')
                self.stream.flush()  # flush after each message
            except:
                pass


        @classmethod
        def receive(self, data):
            """Return IncomingSMS instance from parsed data."""
            raise NotImplementedError
            
    class MMS:
        
        @classmethod
        def receive(self, data):
            """Return IncomingMMS instance from parsed data."""
            raise NotImplementedError
