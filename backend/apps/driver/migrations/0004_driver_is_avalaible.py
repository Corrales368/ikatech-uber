# Generated by Django 4.1.7 on 2023-02-20 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0003_alter_driverlocation_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='is_avalaible',
            field=models.BooleanField(default=False),
        ),
    ]
