# Generated by Django 5.1.2 on 2024-11-10 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supplier',
            old_name='dreated_at',
            new_name='created_at',
        ),
    ]
