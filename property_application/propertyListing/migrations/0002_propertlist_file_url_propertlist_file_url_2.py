# Generated by Django 5.1.5 on 2025-02-18 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propertyListing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='propertlist',
            name='file_url',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='propertlist',
            name='file_url_2',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
