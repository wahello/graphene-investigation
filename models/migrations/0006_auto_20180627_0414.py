# Generated by Django 2.0.6 on 2018-06-27 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0005_auto_20180627_0320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referee',
            name='games',
            field=models.ManyToManyField(related_name='referees', through='models.RefereeGameComposition', to='models.Game'),
        ),
        migrations.AlterField(
            model_name='team',
            name='games',
            field=models.ManyToManyField(related_name='teams', through='models.TeamGameComposition', to='models.Game'),
        ),
    ]