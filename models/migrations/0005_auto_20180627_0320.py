# Generated by Django 2.0.6 on 2018-06-27 03:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0004_post_post_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='counry',
            new_name='country',
        ),
    ]
