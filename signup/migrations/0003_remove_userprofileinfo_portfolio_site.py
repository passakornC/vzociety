# Generated by Django 2.2.6 on 2019-10-09 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0002_auto_20191009_1452'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='portfolio_site',
        ),
    ]
