# Generated by Django 2.1.5 on 2019-10-27 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0016_auto_20191027_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagepost',
            name='post_pic',
            field=models.ImageField(upload_to='page_post_pic/'),
        ),
    ]
