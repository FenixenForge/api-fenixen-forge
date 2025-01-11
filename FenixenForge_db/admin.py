from django.contrib import admin
from .models import  Product, ProductDescription, ProductUpdate, VersionHistory, ProductLike

admin.site.register(ProductLike)
admin.site.register(Product)
admin.site.register(ProductDescription)
admin.site.register(ProductUpdate)
admin.site.register(VersionHistory)
