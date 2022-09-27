from django import forms
from django.contrib.auth.forms import UserCreationForm
from editor_app.models import CustomUser

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
		model = CustomUser
		fields = UserCreationForm.Meta.fields + ("email", )

class UserProfileForm(forms.ModelForm):
	class Meta(UserCreationForm):
		model = CustomUser
		fields = ("first_name", "last_name")