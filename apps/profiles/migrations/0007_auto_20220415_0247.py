# Generated by Django 3.2.7 on 2022-04-15 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_auto_20220414_2245'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Game',
        ),
        migrations.DeleteModel(
            name='GameCategory',
        ),
    ]
