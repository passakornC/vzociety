# Generated by Django 2.2.6 on 2019-10-10 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0010_auto_20191010_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='profile_pic',
            field=models.ImageField(blank=True, default='profile_pics/kishan.jpg', upload_to='media/profile_pics/'),
        ),
    ]
