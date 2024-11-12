# Generated by Django 5.1 on 2024-11-10 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaultapp', '0020_rename_images_propertyinfo_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='propertyinfo',
            old_name='price',
            new_name='buy',
        ),
        migrations.AddField(
            model_name='propertyinfo',
            name='rent',
            field=models.FloatField(default=0),
        ),
    ]
