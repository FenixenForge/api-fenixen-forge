# Generated by Django 5.1.4 on 2025-01-03 03:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FenixenForge_db', '0006_productlike'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='likes',
        ),
        migrations.AlterField(
            model_name='productlike',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FenixenForge_db.product'),
        ),
    ]
