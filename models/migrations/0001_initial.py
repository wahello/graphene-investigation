# Generated by Django 2.0.6 on 2018-06-25 01:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Athlete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.PositiveSmallIntegerField()),
                ('weight', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favorite_strategy', models.CharField(choices=[('FOUR_FOUR_TWO', 'Four Four Two'), ('FIVE_THREE_ONE', 'Five Four One'), ('FIVE_THREE_TWO', 'Five Three Two')], default='FOUR_FOUR_TWO', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bodytext', models.TextField()),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('population', models.PositiveIntegerField()),
                ('annual_gdp', models.BigIntegerField()),
                ('national_anthem_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('location', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('GROUP_A', 'Group A'), ('GROUP_B', 'Group B'), ('GROUP_C', 'Group C'), ('GROUP_D', 'Group D'), ('GROUP_E', 'Group E'), ('GROUP_F', 'Group F')], max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Referee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poor_eyesight', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='RefereeGameComposition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(choices=[('MAIN', 'Main'), ('ASSISTANT', 'Assistant'), ('GOAL_LINE', 'Goal Line')], default='MAIN', max_length=15)),
                ('game', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='referee_game_compositions', to='models.Game')),
                ('referee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='referee_game_compositions', to='models.Referee')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ranking', models.PositiveSmallIntegerField()),
                ('counry', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='team', to='models.Country')),
            ],
        ),
        migrations.CreateModel(
            name='TeamGameComposition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_home', models.BooleanField(default=False)),
                ('result', models.CharField(blank=True, choices=[('WIN', 'Win'), ('LOSE', 'Lose'), ('DRAW', 'Draw')], max_length=5, null=True)),
                ('game', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='team_game_compositions', to='models.Game')),
                ('team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='team_game_compositions', to='models.Team')),
            ],
        ),
        migrations.AddField(
            model_name='team',
            name='games',
            field=models.ManyToManyField(through='models.TeamGameComposition', to='models.Game'),
        ),
        migrations.AddField(
            model_name='team',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teams', to='models.Group'),
        ),
        migrations.AddField(
            model_name='referee',
            name='games',
            field=models.ManyToManyField(through='models.RefereeGameComposition', to='models.Game'),
        ),
        migrations.AddField(
            model_name='referee',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='referee', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(related_name='posts', to='models.Tag'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comments', to='models.Post'),
        ),
        migrations.AddField(
            model_name='coach',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='coaches', to='models.Team'),
        ),
        migrations.AddField(
            model_name='coach',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='coach', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='athlete',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='athletes', to='models.Team'),
        ),
        migrations.AddField(
            model_name='athlete',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='athlete', to=settings.AUTH_USER_MODEL),
        ),
    ]