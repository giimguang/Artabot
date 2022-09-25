from django import forms
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    email = forms.CharField(max_length=100,widget= forms.EmailInput(
		attrs={
			'autocomplete': 'off'
		}
	))
    username = forms.CharField(max_length=100,widget= forms.TextInput(
		attrs={
			'autocomplete': 'off'
		}
	))
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email", )