# Generated by Django 5.1.2 on 2024-11-06 02:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaultapp', '0007_user_isdoctor_alter_analysisresult_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analysisresult',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 6, 2, 8, 24, 509835, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='testresult',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 6, 2, 8, 24, 509835, tzinfo=datetime.timezone.utc)),
        ),
    ]
