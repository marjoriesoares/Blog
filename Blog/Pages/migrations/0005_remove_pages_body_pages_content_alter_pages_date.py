# Generated by Django 4.1 on 2022-09-26 15:15

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0004_alter_pages_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pages',
            name='body',
        ),
        migrations.AddField(
            model_name='pages',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(default='use timezone.now'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pages',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
