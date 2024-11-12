# Generated by Django 5.1.2 on 2024-11-06 09:55

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaultapp', '0014_alter_analysisresult_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analysisresult',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 6, 9, 55, 2, 757537, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='testresult',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 6, 9, 55, 2, 757537, tzinfo=datetime.timezone.utc)),
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frequency', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prescription', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
