from dataclasses import field
from distutils.text_file import TextFile
from django import forms
from .models import User_Report

class UserReportForm(forms.ModelForm):
    email = forms.CharField(max_length=100,widget= forms.TextInput(
        attrs={
            'class':'report_email',
            'autocomplete':'off',
            'requried': 'false'
        }
	))
    report = forms.CharField(max_length=100,widget= forms.TextInput(
        attrs={
            'class':'report_detial',
            'autocomplete':'off',
            'requried': 'false'
        }
	))
    class Meta:
        model = User_Report
        fields = ['email','report']
        label = {
            'email': 'Email',
            'report': 'Report'
        }