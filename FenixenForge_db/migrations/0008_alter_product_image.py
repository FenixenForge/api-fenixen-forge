# Generated by Django 5.1.4 on 2025-01-03 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FenixenForge_db', '0007_remove_product_likes_alter_productlike_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/products/images/'),
        ),
    ]
