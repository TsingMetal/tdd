import time
import hashlib
from xml.etree import ElementTree as ET

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import View
from django.template import loader, Context

AppSecret = 'f01119eb56e10adaf7a971e9c9c6b740'

class WeChat(View):

    @csrf_exempt
    def dispatch(self, *args, **kargs):
        return super(WeChat, self).dispatch(*args, **kargs)

    def get(self, request):
        signature = request.GET.get('signature', '')
        timestamp = request.GET.get('timestamp', '')
        nonce = request.GET.get('nonce', '')
        echostr = request.GET.get('echostr', 'test')

        token = 'tsingmetal'

        hashstr = ''.join(sorted([timestamp, nonce, token]))

        hashstr = hashlib.sha1(hashstr.encode('utf-8')).hexdigest()

        if hashstr == signature:
            return HttpResponse(echostr)
        return HttpResponse('nihao')

    def post(self, request):
        return HttpResponse("ni hao")
