# Generated by Django 4.2.1 on 2023-05-30 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='prority',
            new_name='priority',
        ),
    ]
