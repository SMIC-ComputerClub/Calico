# Generated by Django 3.2.3 on 2022-09-21 03:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 9, 21, 3, 21, 17, 141523, tzinfo=utc)),
        ),
    ]