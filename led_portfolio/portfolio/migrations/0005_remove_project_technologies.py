# Generated by Django 5.1.5 on 2025-02-23 21:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_alter_personalinfo_bio_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='technologies',
        ),
    ]
