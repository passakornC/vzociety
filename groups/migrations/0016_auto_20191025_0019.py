# Generated by Django 2.1.5 on 2019-10-24 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0015_grouprequestinfo_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grouprequestinfo',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.Group'),
        ),
    ]
