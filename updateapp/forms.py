from django import forms
from .models import User,Neighborhood,Business,Update,Health

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Update
        exclude = ['writer']

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = '__all__'

class HealthForm(forms.ModelForm):
    class Meta:
        model = Health
        fields = '__all__'

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserStatus
        exclude = ['user']

class NeighborhoodForm(forms.ModelForm):
    class Meta:
        model = UserStatus
        exclude = ['user','user_image','user_email']
