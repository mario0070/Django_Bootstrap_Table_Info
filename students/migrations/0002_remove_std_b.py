# Generated by Django 3.2.9 on 2022-08-30 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='std',
            name='b',
        ),
    ]