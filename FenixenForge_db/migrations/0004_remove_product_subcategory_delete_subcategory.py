# Generated by Django 5.1.4 on 2025-01-01 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FenixenForge_db', '0003_alter_product_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='subcategory',
        ),
        migrations.DeleteModel(
            name='Subcategory',
        ),
    ]
