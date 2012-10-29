# encoding: utf-8


class BaseBackend:
    """
    Base class for sms backend implementations.

    Subclasses must at least overwrite send().
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
