# Generated by Django 2.2.5 on 2019-09-28 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0021_proregisteringo_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proregisteringo',
            name='email',
            field=models.TextField(max_length=20),
        ),
    ]
