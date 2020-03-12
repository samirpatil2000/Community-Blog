from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import models

from.models import Post

#
# class PostUpdateForm(forms.ModelForm):
#     class Meta:
#         model=Post
#         fields = ['title','sub_title','attractiv_lines','content','blog_image_1','content_2']
