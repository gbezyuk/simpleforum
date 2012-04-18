from django.utils.translation import ugettext_lazy as _, ugettext as __
from django import forms

class LoginForm(forms.Form):
	username = forms.CharField(max_length=100, label=_('username'))
	password = forms.CharField(widget=forms.PasswordInput, max_length=100, label=_('password'))