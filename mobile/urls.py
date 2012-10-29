from django.conf.urls.defaults import *

from views import *

urlpatterns = patterns('',
    url(r'^receive_sms$', receive_sms),
    url(r'^receive_mms$', receive_mms)
)
