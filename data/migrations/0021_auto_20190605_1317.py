# Generated by Django 2.1.5 on 2019-06-05 07:47

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0020_auto_20190605_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='longDesc',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
