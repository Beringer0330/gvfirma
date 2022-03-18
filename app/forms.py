from collections import UserList
from django import  forms
from django.db.models import fields
from django.forms import widgets
from .models import Landing
from captcha.fields import ReCaptchaField


class LandingForm(forms.ModelForm):
    class Meta:
        model= Landing
        fields='__all__'
        widgets={
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'correo': forms.TextInput(attrs={'type':'email','class':'form-control'}),
            'numero': forms.TextInput(attrs={'type':'number','class':'form-control'}),   
            'asunto': forms.TextInput(attrs={'class':'form-control'}),
        }

class FormWithCaptcha(forms.Form):
    captcha = ReCaptchaField()