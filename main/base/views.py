from django.shortcuts import render
from .models import Usuario

def loginPage(request):
    return render(request, 'base/login.html')
    


def registerPage(request):
    user = Usuario()
    
    return render(request, 'base/register.html')


def welcomePage(request):
    return render(request, 'base/welcome.html')
