# Generated by Django 5.1 on 2024-11-10 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaultapp', '0024_propertyinfo_bathrooms_propertyinfo_bedrooms_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='propertyinfo',
            name='area',
            field=models.FloatField(default=0),
        ),
    ]
