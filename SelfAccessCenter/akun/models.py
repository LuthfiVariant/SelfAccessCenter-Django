from django.db import models

# Create your models here.

class Akun(models.Model):
    nama        = models.CharField(max_length=50,)
    nim         = models.CharField(max_length=7)
    password    = models.CharField(max_length=100)
    email       = models.EmailField(max_length=254,)
    verifikasi  = models.BooleanField(default=False)