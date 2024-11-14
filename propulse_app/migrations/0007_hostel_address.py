# Generated by Django 5.1 on 2024-11-14 14:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propulse_app', '0006_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='hostel',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='propulse_app.address'),
        ),
    ]