# Generated by Django 2.1.7 on 2019-03-29 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20190329_0935'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foodmania',
            name='Restaurant_Description',
        ),
        migrations.RemoveField(
            model_name='foodmania',
            name='Restaurant_Name',
        ),
        migrations.RemoveField(
            model_name='foodmania',
            name='Restaurant_email',
        ),
    ]
