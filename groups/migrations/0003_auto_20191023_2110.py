# Generated by Django 2.1.5 on 2019-10-23 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_groupprofileinfo_fee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupprofileinfo',
            name='fee',
            field=models.IntegerField(blank=True, default=0, max_length=1000),
        ),
    ]