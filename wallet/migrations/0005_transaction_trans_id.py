# Generated by Django 2.0.5 on 2019-10-30 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0004_auto_20191030_2009'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='trans_id',
            field=models.IntegerField(default=0, unique=True),
        ),
    ]
