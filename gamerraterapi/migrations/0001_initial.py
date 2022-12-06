# Generated by Django 4.1.3 on 2022-12-05 23:25

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('designer', models.CharField(max_length=50)),
                ('year_released', models.DateField()),
                ('number_of_players', models.IntegerField()),
                ('play_time', models.IntegerField()),
                ('rec_age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=50)),
                ('bio', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=750)),
                ('game_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamerraterapi.game')),
                ('player_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamerraterapi.player')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('game_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamerraterapi.game')),
                ('player_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamerraterapi.player')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.ImageField(upload_to='images/player_images')),
                ('game_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamerraterapi.game')),
                ('player_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamerraterapi.player')),
            ],
        ),
        migrations.CreateModel(
            name='GameCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamerraterapi.category')),
                ('game_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamerraterapi.game')),
            ],
        ),
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.ImageField(upload_to='images/avatars')),
                ('player_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamerraterapi.player')),
            ],
        ),
    ]