# Generated by Django 2.0.5 on 2019-10-30 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0018_userprofileinfo_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='group_count',
            field=models.IntegerField(default=0),
        ),
    ]
