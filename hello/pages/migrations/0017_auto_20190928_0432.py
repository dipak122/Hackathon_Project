# Generated by Django 2.2.5 on 2019-09-27 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0016_auto_20190928_0409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logtable',
            name='opt',
            field=models.IntegerField(),
        ),
    ]
