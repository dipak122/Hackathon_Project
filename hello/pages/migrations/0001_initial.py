# Generated by Django 2.2.5 on 2019-09-25 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='listdb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=10)),
                ('city', models.TextField(max_length=10)),
            ],
        ),
    ]
