# Generated by Django 5.1 on 2024-11-13 06:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propulse_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='utility',
            options={'verbose_name_plural': 'Utilities'},
        ),
        migrations.AlterField(
            model_name='hostel',
            name='more_media',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='get_hostels', to='propulse_app.hostelmedia'),
        ),
        migrations.AlterField(
            model_name='hostel',
            name='picture1',
            field=models.ImageField(blank=True, null=True, upload_to='hostel_pictures/'),
        ),
        migrations.AlterField(
            model_name='hostel',
            name='picture2',
            field=models.ImageField(blank=True, null=True, upload_to='hostel_pictures/'),
        ),
        migrations.AlterField(
            model_name='hostel',
            name='picture3',
            field=models.ImageField(blank=True, null=True, upload_to='hostel_pictures/'),
        ),
        migrations.AlterField(
            model_name='hostel',
            name='picture4',
            field=models.ImageField(blank=True, null=True, upload_to='hostel_pictures/'),
        ),
        migrations.AlterField(
            model_name='hostel',
            name='picture5',
            field=models.ImageField(blank=True, null=True, upload_to='hostel_pictures/'),
        ),
        migrations.AlterField(
            model_name='hostelmedia',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='hostel_pictures/'),
        ),
        migrations.AlterField(
            model_name='hostelmedia',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='hostel_videos/'),
        ),
    ]
