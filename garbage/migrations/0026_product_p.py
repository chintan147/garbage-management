# Generated by Django 2.0 on 2021-03-26 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('garbage', '0025_auto_20210326_1707'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='p',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='garbage.Admin'),
        ),
    ]
