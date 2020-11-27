from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse


def login(request):
    return render(request, 'login.html')
    # noinspection PyUnreachableCode
    '''username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/account')
        else:
            return render(request, 'loginFail.html')'''
