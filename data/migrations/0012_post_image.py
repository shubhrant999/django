# Generated by Django 2.1.5 on 2019-05-31 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0011_auto_20190531_1730'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
