# Generated by Django 3.0.5 on 2020-07-25 01:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_images_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='images',
            name='url',
        ),
    ]
