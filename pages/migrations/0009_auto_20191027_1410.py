# Generated by Django 2.1.5 on 2019-10-27 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_auto_20191027_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagepost',
            name='image',
            field=models.ImageField(upload_to='page_post_pic'),
        ),
    ]
