# Generated by Django 2.0 on 2021-04-03 05:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('garbage', '0039_auto_20210403_1055'),
    ]

    operations = [
        migrations.RenameField(
            model_name='request',
            old_name='Date_Time',
            new_name='Date',
        ),
    ]
