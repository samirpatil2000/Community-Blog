# Generated by Django 3.0.2 on 2020-02-11 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0006_auto_20200210_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='blog_image',
            field=models.ImageField(default='default_1.png', upload_to='blog_pics'),
        ),
        migrations.AlterField(
            model_name='post',
            name='blog_image_1',
            field=models.ImageField(default='default.jpg', upload_to='blog_pics'),
        ),
    ]
