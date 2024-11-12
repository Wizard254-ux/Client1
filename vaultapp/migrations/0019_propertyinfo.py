# Generated by Django 5.1 on 2024-11-10 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaultapp', '0018_clientinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='propertyInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('location', models.CharField(max_length=100)),
                ('images', models.ImageField(upload_to='property_images/')),
                ('description', models.CharField(max_length=100)),
                ('propertyType', models.CharField(max_length=50)),
            ],
        ),
    ]