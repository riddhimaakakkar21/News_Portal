from django import forms
from django.forms import ModelForm
from NewsApp.models import User , User_hrs_data 


class display_forms(ModelForm):
     
     class Meta:
        model = User
        fields ='__all__'


class display_hrs_forms(forms.Form):
  class Meta:
        model = User
        fields ='__all__'


