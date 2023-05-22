# Generated by Django 4.2.1 on 2023-05-22 10:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MinValueValidator(9)]),
        ),
    ]
