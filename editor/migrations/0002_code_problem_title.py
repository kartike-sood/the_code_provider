# Generated by Django 3.1.1 on 2020-09-23 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='code',
            name='problem_title',
            field=models.TextField(blank=True, null=True),
        ),
    ]
