# Generated by Django 2.1.5 on 2019-10-27 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_pagepost_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagepost',
            name='page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.PageProfileInfo'),
        ),
    ]
