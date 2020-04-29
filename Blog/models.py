from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image


# Create your models here.
class Post(models.Model):

    title=models.CharField(max_length=50)
    sub_title=models.CharField(default="This is the subtitle of the post ",max_length=150)
    attractiv_lines=models.TextField(default="This is attractive lines that attract the people ",max_length=1000)
    content=models.TextField(max_length=4000)
    content_2=models.TextField(default="add here")
    date_posted=models.DateTimeField(default=timezone.now)
   # blog_image=models.ImageField(default='profile_icon.png',upload_to='blog_pics')
    #blog_image=models.ImageField(default='default_1.png',upload_to='blog_pics')
   # blog_image_1=models.ImageField(default='default.jpg',upload_to='media')
    blog_image_1=models.ImageField(default='default.jpg',upload_to='blog_pics')

    #blog_image_1=models.ImageField(upload_to='blog_pics')
    author =models.ForeignKey(User,on_delete=models.CASCADE)   #this for if we delete the user the post will also deleted and not vice versa



    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})

    # def save(self,*args,**kwargs):
    #     super().save(*args,**kwargs)
    #    # img_1=Image.open(self.blog_image.path)
    #     img_2=Image.open(self.blog_image_1.path)
    #     #
    #     #
    #     # if img_1.height > 400 or img_1.width > 400 or img_2.height > 400 or img_2.width > 400 :
    #     #     output_size=(400,400)
    #     #     img_1.thumbnail(output_size)
    #     #     img_2.thumbnail(output_size)
    #     #     img_1.save(self.blog_image.path)
    #     #     img_2.save(self.blog_image_1.path)
    #
    #
    #     #
    #     if  img_2.height > 400 or img_2.width > 400 :
    #         output_size=(400,400)
    #       #  img_1.thumbnail(output_size)
    #         img_2.thumbnail(output_size)
    #        # img_1.save(self.blog_image.path)
    #         img_2.save(self.blog_image_1.path)
    #
    # #


