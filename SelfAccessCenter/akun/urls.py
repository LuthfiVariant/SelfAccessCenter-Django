from django.urls import path

from . import views

urlpatterns = [
    path('daftar/', views.buat_akun_view, name='daftar'),
]