# Generated by Django 5.1.4 on 2024-12-31 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FenixenForge_db', '0002_category_product_downloads_product_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
