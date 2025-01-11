from django.db import models

class Product(models.Model):
    """Modelo principal del producto."""
    name = models.CharField(max_length=100, unique=True)  # Unique para evitar conflictos en las rutas
    description = models.TextField()
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    downloads = models.PositiveIntegerField(default=0)

    def increase_downloads(self):
        self.downloads += 1
        self.save(update_fields=["downloads"])

    def __str__(self):
        return self.name


class ProductDescription(models.Model):
    """Descripciones adicionales con imágenes asociadas."""
    titulo = models.CharField(max_length=100, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="descriptions")
    description = models.TextField()
    image_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"Description for {self.product.name}"

class ProductLike(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('product', 'ip_address')

class ProductUpdate(models.Model):
    """Actualizaciones del producto, como un blog."""
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="updates")
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Update {self.title} for {self.product.name}"


class VersionHistory(models.Model):
    """Historial de versiones del producto."""
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="version_history")
    version = models.CharField(max_length=50)
    url_download = models.URLField()
    likes = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} - Version {self.version}"
