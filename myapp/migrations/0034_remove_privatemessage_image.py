# Generated by Django 4.0.5 on 2022-07-31 05:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0033_privatemessage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='privatemessage',
            name='image',
        ),
    ]