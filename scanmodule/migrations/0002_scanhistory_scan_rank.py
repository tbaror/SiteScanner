# Generated by Django 3.1 on 2020-08-30 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scanmodule', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='scanhistory',
            name='scan_rank',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
