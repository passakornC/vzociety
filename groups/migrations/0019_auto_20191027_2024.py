# Generated by Django 2.1.5 on 2019-10-27 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0018_groupinvitation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupprofileinfo',
            name='group_pic',
            field=models.ImageField(blank=True, default='default_pic/default_pic.jpg', upload_to='group_profile_pics/'),
        ),
    ]