# Generated by Django 2.2.5 on 2019-09-27 09:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_auto_20190927_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='logtable',
            name='address',
            field=models.TextField(default='no', max_length=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logtable',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
