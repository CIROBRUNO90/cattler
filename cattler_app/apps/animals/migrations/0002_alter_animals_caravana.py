# Generated by Django 4.0.3 on 2022-04-08 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animals',
            name='caravana',
            field=models.IntegerField(null=True, unique=True),
        ),
    ]
