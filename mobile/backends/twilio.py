# encoding: utf-8
import twilio.twiml

from django.http import QueryDict

from twilio.rest import TwilioRestClient

from mobile.backends.base import BaseBackend
import mobile.models

class Backend(BaseBackend):
    """Twilio Gate Backend."""

    class SMS:

        @classmethod
        def send(self, recipient, sender, message):
            """
            Send an SMS and return its initial delivery status code.

            See twilio-python Documentation: https://github.com/twilio/twilio-python

            """

            client = TwilioRestClient()

            message = client.messages.create(
                to=recipient,
                from_=sender,
                body=message
            )

            return [message.Status, message.sid, message.ErrorCode, message.ErrorMessage]

        @classmethod
        def receive(self, data):
            """Return IncomingSMS instance from parsed data."""

            data = QueryDict(data).copy()

            sms = mobile.models.IncomingSMS(
                message_id=data.get('MessageSid'),
                country=data.get('FromCountry', None),
                sender=data.get('From'),
                recipient=data.get('To'),
                message=data.get('Body'),
                source=data
            )

            return sms.save()

    class MMS:

        @classmethod
        def receive(self, data):
            """Return IncomingMMS instance from parsed data."""
            raise NotImplementedError
