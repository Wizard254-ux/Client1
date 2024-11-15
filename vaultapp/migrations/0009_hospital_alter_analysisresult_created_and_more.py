# Generated by Django 5.1.2 on 2024-11-06 02:57

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaultapp', '0008_alter_analysisresult_created_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('uuid', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='analysisresult',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 6, 2, 57, 56, 165504, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='testresult',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 6, 2, 57, 56, 165504, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AddField(
            model_name='user',
            name='Hospital',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='vaultapp.hospital'),
        ),
    ]
