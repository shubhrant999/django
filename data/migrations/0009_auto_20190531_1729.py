# Generated by Django 2.1.5 on 2019-05-31 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0008_auto_20190531_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_type',
            field=models.CharField(choices=[('0', 'Rent'), ('1', 'Sale')], max_length=1),
        ),
    ]
