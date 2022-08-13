# Generated by Django 4.0.5 on 2022-07-23 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_profile_followers_profile_following_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ('-created',)},
        ),
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ('-created',)},
        ),
        migrations.AlterModelOptions(
            name='topic',
            options={'ordering': ('-name',)},
        ),
        migrations.AlterField(
            model_name='room',
            name='title',
            field=models.TextField(max_length=10000),
        ),
    ]