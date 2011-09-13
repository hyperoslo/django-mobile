from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from django_api_utilities.decorators import methods_supported, authentication_required

from backends import backend
from settings import GATE_USERNAME, GATE_PASSWORD

@methods_supported(['POST'])
#@authentication_required(GATE_USERNAME, GATE_PASSWORD)
@csrf_exempt
def receive_sms(request):
    backend.SMS.receive(request.raw_post_data)
    
    return HttpResponse(status=200)
    
def receive_mms(request):
    backend.MMS.receive(request.raw_post_data)

    return HttpResponse(status=200)