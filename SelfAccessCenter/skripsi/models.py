from django.db import models

# Create your models here.

class Skripsi(models.Model):

    judul       = models.CharField(max_length=50)
    penulis     = models.CharField(max_length=50)
    tahun       = models.IntegerField()
    abstrak     = models.TextField()
    berkas      = models.FileField()
