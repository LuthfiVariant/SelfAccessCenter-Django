from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class MyAccountManager(BaseUserManager):
    def create_user(self, email, nim, password=None):
        if not email:
            raise ValueError("Harap masukkan email Anda.")


class Account(AbstractBaseUser):
    PRODI = (
        ("Pendidikan", "Pendidikan"),
        ("Sastra", "Sastra")
    )
    nama        = models.CharField(max_length=50, null=True, unique=True)
    nim         = models.CharField(max_length=7, null=True, unique=True)
    prodi       = models.CharField(max_length=50, choices=PRODI, null=True)
    password    = models.CharField(max_length=50, null=True)
    email       = models.EmailField(max_length=254, null=True, unique=True)
    is_admin    = models.BooleanField(default=False, null=True)
    is_active    = models.BooleanField(default=False, null=True)
    is_staff    = models.BooleanField(default=False, null=True)
    is_superuser    = models.BooleanField(default=False, null=True)

    USERNAME_FIELD = 'nim'
    REQUIRED_FIELDS = ['username']


    def __str__(self):
        return self.nama

class Document(models.Model):
    KATEGORI = (
        ("Pendidikan", "Pendidikan"),
        ("Non-Pendidikan", "Non-Pendidikan")
    )


    judul = models.CharField(max_length=200, null=True)
    kategori = models.CharField(max_length=50, choices=KATEGORI, null=True)
    penulis = models.CharField(max_length=50, null=True)
    abstrak = models.TextField(max_length=5000, null=True)
    keywords = models.CharField(max_length=100, null=True)
    berkas = models.FileField(null=True)

    def __str__(self):
        return self.judul


