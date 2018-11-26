from django import forms
from .models import UserProfile,Neighborhood,Business,Update,Health

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
        model = UserProfile
        exclude = ['user']

class NeighborhoodForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user','user_image','user_email']
