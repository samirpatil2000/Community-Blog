from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from . import models
from.models import Profile

class UserRegisterForm(UserCreationForm):
    #email_na=models.EmailField(required=True)
    first_name=forms.CharField(max_length=30,required=False,help_text='Enter Your Name ')
    last_name=forms.CharField(max_length=30,required=False,help_text='Enter Your Surname')
    email=forms.EmailField(help_text='Enter Your  Valid email address')
    phone_number=forms.IntegerField(help_text='enter valid phone number ')
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','phone_number','password1','password2']

    def save(self, commit=True):
        user=super(UserRegisterForm,self).save(commit=True)
        user.first_name= self.cleaned_data['first_name']
        user.last_name=self.cleaned_data['last_name']
        user.phone_number=self.cleaned_data['phone_number']
        if commit:
            user.save()

        return user



class UserUpadeteForm(forms.ModelForm):
    email=forms.EmailField()

    first_name=forms.CharField(max_length=30,required=False,help_text='Enter Your Name ')
    last_name=forms.CharField(max_length=30,required=False,help_text='Enter Your Surname')

    class Meta:
        model = User
        fields=['username','first_name','last_name','email']

    def save(self, commit=True):
        user=super(UserUpadeteForm,self).save(commit=True)
        user.first_name= self.cleaned_data['first_name']
        user.last_name=self.cleaned_data['last_name']
        if commit:
            user.save()
        return user


class ProfileUpdateForm(forms.ModelForm):

    class Meta:

        model= Profile
        fields=['image']
