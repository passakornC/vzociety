# Generated by Django 2.2.2 on 2019-06-17 11:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_messages', '0002_auto_20160607_0852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sent_messages', to=settings.AUTH_USER_MODEL, verbose_name='Sender'),
        ),
    ]
