# Generated by Django 3.1.1 on 2020-09-16 12:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coder',
            fields=[
                ('code_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=30)),
                ('website', models.CharField(max_length=30)),
                ('code_title', models.CharField(max_length=30)),
                ('preference', models.CharField(max_length=7)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
