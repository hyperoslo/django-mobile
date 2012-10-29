# encoding: utf-8

from django.db import models

from backends import backend
from settings import DEFAULT_INTERNATIONAL_PREFIX, SHORT_CODE


class OutgoingSMS(models.Model):
    recipient = models.CharField('mottaker', max_length=255)
    sender = models.CharField('avsender', max_length=255, default=SHORT_CODE)
    message = models.TextField('beskjed')
    sent = models.BooleanField('sendt')
    price = models.IntegerField('pris', default=0)
    country = models.CharField('land', max_length=255, default="NO")
    delivery_status = models.IntegerField('leveringsstatus', null=True, blank=True)
    delivery_message = models.TextField('leveringsmelding', blank=True)
    sent_at = models.DateTimeField('sendingsdato', auto_now_add=True)

    def send(self, commit=True):
        """
        Send the SMS and populate delivery status, message and sent-flag.

        :param commit: Saves outgoing sms to database after sending
        """

        self.clean()

        delivery_status, delivery_message = backend.SMS.send(
            recipient=self.recipient,
            sender=self.sender,
            price=self.price,
            country=self.country,
            message=self.message
        )

        self.delivery_status = delivery_status
        self.delivery_message = delivery_message
        self.sent = True

        if commit:
            self.save()

    def clean(self):
        """Ensure the recipient has an international prefix."""
        if len(self.recipient) <= 8:
            self.recipient = '%s%s' % (DEFAULT_INTERNATIONAL_PREFIX, self.recipient)

    def save(self, *args, **kwargs):
        self.clean()
        super(OutgoingSMS, self).save(*args, **kwargs)

    def __unicode__(self):
        return 'SMS til %s' % self.recipient

    class Meta:
        verbose_name = "Sendt SMS"
        verbose_name_plural = "Sendte SMS"


class IncomingSMS(models.Model):
    message_id = models.CharField('gateway message id', max_length=255, blank=True)
    recipient = models.CharField('mottaker', max_length=255)
    sender = models.CharField('avsender', max_length=255)
    message = models.TextField('beskjed')
    country = models.CharField('land', max_length=255, default="NO")
    keyword = models.CharField('nøkkelord', max_length=255, blank=True)
    parameter = models.CharField('parametre', max_length=255, blank=True)
    received_at = models.DateTimeField('mottakelsesdato', auto_now_add=True)
    source = models.TextField('kilde')

    def __unicode__(self):
        return 'SMS fra %s' % self.sender

    class Meta:
        verbose_name = "Mottat SMS"
        verbose_name_plural = "Mottatte SMS"


class IncomingMMS(models.Model):
    message_id = models.CharField('gateway message id', max_length=255, blank=True)
    recipient = models.CharField('mottaker', max_length=255)
    country = models.CharField('land', max_length=255, default="NO")
    sender = models.CharField('avsender', max_length=255)
    subject = models.CharField('emne', max_length=255, blank=True)
    received_at = models.DateTimeField('mottakelsesdato', auto_now_add=True)
    source = models.TextField('kilde')

    def __unicode__(self):
        return 'MMS fra %s' % self.sender

    class Meta:
        verbose_name = "Mottat MMS"
        verbose_name_plural = "Motatte MMS"


class MMSFile(models.Model):
    file = models.FileField('fil', upload_to='uploads/mms_files')
    mms = models.ForeignKey('IncomingMMS', related_name='files')
    content_type = models.CharField('type', max_length=255)

    def __unicode__(self):
        return 'Fil fra %s' % self.mms.sender

    class Meta:
        verbose_name = 'MMS-fil'
        verbose_name_plural = 'MMS-filer'
