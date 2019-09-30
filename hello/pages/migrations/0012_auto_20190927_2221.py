# Generated by Django 2.2.5 on 2019-09-27 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_logtable_des'),
    ]

    operations = [
        migrations.AddField(
            model_name='logtable',
            name='time',
            field=models.TextField(default=' ', max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='logtable',
            name='date',
            field=models.TextField(max_length=10),
        ),
    ]