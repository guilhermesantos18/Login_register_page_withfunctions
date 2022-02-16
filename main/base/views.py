from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from .models import Usuario
from .forms import LoginPage, RegisterPage


def loginPage(request):
    if request.method == 'POST':
        loginform == LoginPage(request.POST)
    else:
        loginform = LoginPage()

    return render(request, 'base/login.html', {'loginform': loginform})
    

def registerPage(request):
    if request.method == 'POST':    
        registerform = RegisterPage(request.POST)
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        user = Usuario(name=name, eml=email, passw=password)
        if user is not None:
            return HttpResponseRedirect('http://127.0.0.1:8000/')
        else:
            return HttpResponse('Usuário não registado!')
    else:
        registerform = RegisterPage()



    return render(request, 'base/register.html', {'registerform': registerform})


def welcomePage(request):
    return render(request, 'base/welcome.html')
