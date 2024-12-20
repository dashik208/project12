from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
fields = ['username', 'email', 'number', 'password1', 'password2']
def clean_email(self):
    email = self.cleaned_data.get('email')
    if CustomUser.objects.filter(email=email).exists():
        raise forms.ValidationError('Этот email уже используется.')
    return email