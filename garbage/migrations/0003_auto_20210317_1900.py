# Generated by Django 2.0 on 2021-03-17 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garbage', '0002_auto_20210317_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='OTP',
            field=models.IntegerField(),
        ),
    ]
