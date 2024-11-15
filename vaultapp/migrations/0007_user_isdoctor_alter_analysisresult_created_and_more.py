# Generated by Django 5.1.2 on 2024-11-06 01:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaultapp', '0006_alter_analysisresult_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='isDoctor',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='analysisresult',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 6, 1, 35, 39, 220107, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='testresult',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 6, 1, 35, 39, 220107, tzinfo=datetime.timezone.utc)),
        ),
    ]
