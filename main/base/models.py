from django.db import models
from django.contrib.auth.models import User
from numpy import mask_indices


class Usuario(User):
    name = models.CharField(max_length=200)
    eml = models.EmailField(max_length=200)
    passw = models.CharField(max_length=200)
    

