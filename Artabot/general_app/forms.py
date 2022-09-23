from dataclasses import field
from distutils.text_file import TextFile
from django import forms
from .models import User_Report

class UserReportForm(forms.ModelForm):
    class Meta:
        model = User_Report
        fields = ['email','report']
        label = {
            'email': 'Email',
            'report': 'Report'
        }