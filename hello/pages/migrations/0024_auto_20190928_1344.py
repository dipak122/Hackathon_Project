# Generated by Django 2.2.5 on 2019-09-28 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0023_auto_20190928_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proregisteringo',
            name='address',
            field=models.TextField(max_length=80),
        ),
        migrations.AlterField(
            model_name='registeringo',
            name='address',
            field=models.TextField(max_length=80),
        ),
        migrations.AlterField(
            model_name='registeringo',
            name='email',
            field=models.TextField(max_length=80),
        ),
    ]