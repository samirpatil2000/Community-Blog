# Generated by Django 3.0.3 on 2020-03-07 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0011_remove_post_blog_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content_2',
            field=models.TextField(default='add here'),
        ),
    ]
