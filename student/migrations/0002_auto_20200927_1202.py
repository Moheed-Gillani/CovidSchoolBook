# Generated by Django 3.1.1 on 2020-09-27 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='fee',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='salary',
        ),
        migrations.AddField(
            model_name='student',
            name='address',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='teacher',
            name='address',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
