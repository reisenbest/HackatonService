# Generated by Django 4.2.5 on 2023-11-15 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
