# Generated by Django 2.2.5 on 2019-09-26 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_listdb_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='listdb',
            name='street',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='listdb',
            name='city',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='listdb',
            name='name',
            field=models.CharField(default='', max_length=10),
        ),
    ]
