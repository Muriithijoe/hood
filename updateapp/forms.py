from django import forms
from .models import Neighborhood, User, Business, Update

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Update

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        
