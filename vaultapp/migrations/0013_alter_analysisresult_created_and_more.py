# Generated by Django 5.1.2 on 2024-11-06 06:58

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaultapp', '0012_rename_name_hospital_hospitalname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analysisresult',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 6, 6, 58, 40, 89617, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='testresult',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 6, 6, 58, 40, 88616, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='Hospital',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='User', to='vaultapp.hospital'),
        ),
    ]
