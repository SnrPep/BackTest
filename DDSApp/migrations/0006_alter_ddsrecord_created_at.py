# Generated by Django 4.2.20 on 2025-04-09 13:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('DDSApp', '0005_remove_ddsrecord_created_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ddsrecord',
            name='created_at',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
