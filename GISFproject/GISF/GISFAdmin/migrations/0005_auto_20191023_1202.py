# Generated by Django 2.2.5 on 2019-10-23 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GISFAdmin', '0004_auto_20191023_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='password',
            field=models.CharField(max_length=500),
        ),
    ]
