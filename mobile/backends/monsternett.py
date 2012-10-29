# encoding: utf-8
from mobile.backends.base import BaseBackend


class Backend(BaseBackend):
    """
    Monsternett backend
    """

    class SMS:

        @classmethod
        def send(self, recipient, sender, price, country, message):
            """Send an SMS and return its initial delivery status code."""
            raise NotImplementedError

        @classmethod
        def receive(self, data):
            """Return IncomingSMS instance from parsed data."""
            raise NotImplementedError

    class MMS:

        @classmethod
        def receive(self, data):
            """Return IncomingMMS instance from parsed data."""
            raise NotImplementedError
