# Generated by Django 4.1.3 on 2022-12-06 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamerraterapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='name',
            field=models.CharField(default='ducky', max_length=50),
            preserve_default=False,
        ),
    ]
