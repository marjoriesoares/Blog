# Generated by Django 4.1 on 2022-09-23 03:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0007_remove_profile_email_remove_profile_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='name',
            new_name='user',
        ),
    ]
