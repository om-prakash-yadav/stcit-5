from django import forms
from .models import *

class Profileform(forms.ModelForm):
    class Meta:
        model = player
        fields = ('name' , 'userName' , 'mobile', 'institute_name', 'department','year_of_study')