# Generated by Django 5.1.2 on 2024-11-10 05:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='dreated_at',
            new_name='created_at',
        ),
    ]
