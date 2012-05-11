from django.contrib import admin
from models import IncomingSMS, OutgoingSMS, IncomingMMS, MMSFile

class IncomingSMSAdmin(admin.ModelAdmin):
    list_display = ['sender', 'received_at']

admin.site.register(IncomingSMS, IncomingSMSAdmin)

class OutgoingSMSAdmin(admin.ModelAdmin):
    list_display = ['recipient', 'message', 'sent_at', 'sent', 'delivery_status']

admin.site.register(OutgoingSMS, OutgoingSMSAdmin)

class IncomingMMSAdmin(admin.ModelAdmin):
    list_display = ['sender', 'subject', 'received_at']

admin.site.register(IncomingMMS, IncomingMMSAdmin)

admin.site.register(MMSFile)