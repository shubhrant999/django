# Generated by Django 2.1.5 on 2019-05-31 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0007_auto_20190531_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='status',
            field=models.IntegerField(default=0, max_length=1),
        ),
    ]
