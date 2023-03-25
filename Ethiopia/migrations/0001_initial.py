# Generated by Django 4.1.3 on 2023-03-25 10:23

import Ethiopia.models
import cloudinary.models
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('source_name', models.CharField(max_length=100)),
                ('source_url', models.CharField(blank=True, max_length=300)),
                ('file_type', models.CharField(choices=[('image', 'Image'), ('html', 'HTML')], default='image', max_length=9)),
                ('html', models.FileField(blank=True, null=True, upload_to=Ethiopia.models.content_file_name)),
                ('image', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image')),
            ],
        ),
    ]
