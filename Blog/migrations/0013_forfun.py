# Generated by Django 3.0.3 on 2020-04-29 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0012_post_content_2'),
    ]

    operations = [
        migrations.CreateModel(
            name='ForFun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('int', models.IntegerField()),
            ],
        ),
    ]
