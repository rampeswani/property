# Generated by Django 5.1.5 on 2025-01-23 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReferenceMaster',
            fields=[
                ('reference_id', models.AutoField(primary_key=True, serialize=False)),
                ('reference_name', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['reference_id'],
            },
        ),
    ]
