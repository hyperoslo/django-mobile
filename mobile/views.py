from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from backends import backend


@csrf_exempt
def receive_sms(request):
    if request.method != 'POST':
        return HttpResponse(status=405)

    backend.SMS.receive(request.body)
    return HttpResponse(status=200)


@csrf_exempt
def receive_mms(request):
    if request.method != 'POST':
        return HttpResponse(status=405)

    backend.MMS.receive(request.body)
    return HttpResponse(status=200)
