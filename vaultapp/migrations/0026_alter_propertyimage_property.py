# Generated by Django 5.1 on 2024-11-10 23:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaultapp', '0025_propertyinfo_area'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertyimage',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images_read', to='vaultapp.propertyinfo'),
        ),
    ]
