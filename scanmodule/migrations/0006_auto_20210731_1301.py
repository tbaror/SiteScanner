# Generated by Django 3.2.5 on 2021-07-31 10:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scanmodule', '0005_auto_20210710_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteassest',
            name='scan_time_end',
            field=models.DateTimeField(default=datetime.date(2021, 7, 31)),
        ),
        migrations.AlterField(
            model_name='siteassest',
            name='scan_time_start',
            field=models.DateTimeField(default=datetime.date(2021, 7, 31)),
        ),
    ]
