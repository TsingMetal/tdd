from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'sign/index.html')


def login_action(request):
    if request.method =='POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            response = HttpResponseRedirect('/event_manage/')
            #response.set_cookie('user', username, 3600)
            request.session['user'] = username
            return response
        else:
            return render(request, 'sign/index.html', {'error':
                '用户名或者密码不正确!' })


@login_required
def event_manage(request):
    #username = request.COOKIES.get('user', '')
    username = request.session.get('user', '')
    return render(request, 'sign/event_manage.html', {'user': username})
