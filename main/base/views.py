from django.shortcuts import render
from .models import Usuario
from .forms import LoginPage, RegisterPage


def loginPage(request):
    return render(request, 'base/login.html')
    

def registerPage(request):
    user = Usuario()
    if request.POST:    
        registerform = RegisterPage(request.POST)
    
        context = {'registerform': registerform}



    return render(request, 'base/register.html', context)


def welcomePage(request):
    return render(request, 'base/welcome.html')
