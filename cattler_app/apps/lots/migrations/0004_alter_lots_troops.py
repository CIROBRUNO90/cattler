# Generated by Django 4.0.3 on 2022-04-08 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('troops', '0002_alter_troop_troop_id'),
        ('lots', '0003_alter_lots_troops'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lots',
            name='troops',
            field=models.ManyToManyField(default=None, to='troops.troop'),
        ),
    ]
