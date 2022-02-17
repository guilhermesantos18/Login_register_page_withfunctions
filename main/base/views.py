from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from .models import Usuario
from .forms import LoginPage, RegisterPage


def LoginView(request):
    if request.method == 'POST':
        loginform == LoginPage(request.POST)
    else:
        loginform = LoginPage()

    return render(request, 'base/login.html', {'loginform': loginform})
    