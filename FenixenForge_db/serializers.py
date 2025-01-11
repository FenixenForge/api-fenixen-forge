# serializers.py
from rest_framework import serializers
from .models import (
    Product,
    ProductDescription,
    ProductUpdate,
    VersionHistory
)


class ProductDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDescription
        fields = ['id', 'description', 'image', 'titulo']

class VersionHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = VersionHistory
        fields = ['id', 'version', 'url_download', 'created_at']

class ProductMainSerializer(serializers.ModelSerializer):
    descriptions = ProductDescriptionSerializer(many=True, read_only=True)
    url_download = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'description',
            'category',
            'price',
            'image',
            'downloads',
            'descriptions',
            'url_download',
            'created_at',
        ]

    def get_url_download(self, obj):
        latest_version = obj.version_history.order_by('-created_at').first()
        return latest_version.url_download if latest_version else None

class ProductUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductUpdate
        fields = ['id', 'title', 'content', 'created_at']

class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'category', 'price', 'image', 'downloads']
