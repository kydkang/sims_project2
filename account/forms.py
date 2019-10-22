from django import forms
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import User
class UserRegistrationForm(forms.ModelForm): 
    password = forms.CharField(label=_('Password'),  widget=forms.PasswordInput)
    password2 = forms.CharField(label=_('Repeat password'),  widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords do not match.')
        return cd['password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and  User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError('Email addresses must be unique.')
        return email

