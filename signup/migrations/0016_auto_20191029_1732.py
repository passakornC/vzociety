# Generated by Django 2.0.5 on 2019-10-29 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0015_auto_20191020_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='profile_pic',
            field=models.ImageField(blank=True, default='default_pic/default_pic.jpg', upload_to='profile_pics/'),
        ),
    ]
