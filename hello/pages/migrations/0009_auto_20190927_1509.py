# Generated by Django 2.2.5 on 2019-09-27 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_auto_20190927_1109'),
    ]

    operations = [
        migrations.AddField(
            model_name='registeringo',
            name='address',
            field=models.TextField(default='no', max_length=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registeringo',
            name='email',
            field=models.TextField(default='no', max_length=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registeringo',
            name='name',
            field=models.CharField(default='no', max_length=10),
            preserve_default=False,
        ),
    ]
