from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from backends import backend
from settings import GATE_USERNAME, GATE_PASSWORD

@csrf_exempt
def receive_sms(request):
    if request.method != 'POST':
        return HttpResponse(status=405)
    
    backend.SMS.receive(request.raw_post_data)
    return HttpResponse(status=200)

@csrf_exempt
def receive_mms(request):
    if request.method != 'POST':
        return HttpResponse(status=405)
    
    backend.MMS.receive(request.raw_post_data)
    return HttpResponse(status=200)
