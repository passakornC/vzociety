# Generated by Django 2.1.5 on 2019-10-27 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0017_auto_20191027_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pageprofileinfo',
            name='page_pic',
            field=models.ImageField(upload_to='page_profile_pic/'),
        ),
    ]
