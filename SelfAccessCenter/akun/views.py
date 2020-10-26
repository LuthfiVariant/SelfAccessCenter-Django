from django.shortcuts import render

from .forms import AkunForm
# Create your views here.

def buat_akun_view(request):
    form = AkunForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = AkunForm()

    context = {
        'form' : form
    }
    
    return render(request, "akun/daftar.html", context)