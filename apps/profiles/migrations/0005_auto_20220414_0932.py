# Generated by Django 3.2.7 on 2022-04-14 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20220414_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
