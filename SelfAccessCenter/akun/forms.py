from django import forms

from .models import Akun

class AkunForm(forms.ModelForm):
    class Meta:
        model = Akun
        fields = [
            'nama',
            'nim',
            'password',
            'email',
        ]

    def clean_email(self):
        """ memastikan akun hanya bisa mendaftar menggunakan email @student.upi.edu """
        email = self.cleaned_data.get('email')
        if not email.endswith("@student.upi.edu") :
            raise forms.ValidationError("Gunakan Email @student.upi.edu anda")
        else:
            return email