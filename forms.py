from django import forms
from .models import UserProfil

class RegisterForm(forms.ModelForm):

    class Meta:
        model = UserProfil
        fields = (
            'face_id',
            'name',
            'adresse',
            'formation',
            'tel',             
            'bio',
            'image',
        )