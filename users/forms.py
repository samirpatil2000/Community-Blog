from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from.models import Profile

class UserRegisterForm(UserCreationForm):
    first_name=forms.CharField(max_length=30,required=False,help_text='Enter Your Name ')
    last_name=forms.CharField(max_length=30,required=False,help_text='Enter Your Surname')
    email=forms.EmailField(help_text='Enter Your  Valid email address')
    phone_number=forms.IntegerField(help_text='enter valid phone number ')
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','phone_number','password1','password2']



class UserUpadeteForm(forms.ModelForm):
    email=forms.EmailField()

    class Meta:
        model = User
        fields=['username','email']

class ProfileUpdateForm(forms.ModelForm):

    class Meta:

        model= Profile
        fields=['image']
