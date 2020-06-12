from django.contrib import admin

# Register your models here.
from .models import Post,ForFun
admin.site.register(Post)
admin.site.register(ForFun)