from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


def index(request):
    return render(request, 'sign/index.html')


def login_action(request):
    if request.method =='POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if username == 'admin' and password == 'admin123':
            response = HttpResponseRedirect('/event_manage/')
            response.set_cookie('user', username, 3600)
            return response
        else:
            return render(request, 'sign/index.html', {'error':
                '用户名或者密码不正确!' })


def event_manage(request):
    username = request.COOKIES.get('user', '')
    return render(request, 'sign/event_manage.html', {'user': username})
