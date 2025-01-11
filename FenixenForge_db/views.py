import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from .models import Product
from .serializers import ProductMainSerializer, ProductUpdateSerializer, VersionHistorySerializer, ProductDetailSerializer

logger = logging.getLogger(__name__)

class ProductListView(APIView):
    permission_classes = [AllowAny] 

    def get(self, request):
        logger.info("Fetching all products")
        products = Product.objects.all()
        serializer = ProductMainSerializer(products, many=True)
        logger.info(f"Returning {len(serializer.data)} products")
        return Response(serializer.data)

class ProductMainView(APIView):
    permission_classes = [AllowAny] 

    def get(self, request, name):
        logger.info(f"Fetching product details for: {name}")
        product = get_object_or_404(Product, name=name)
        serializer = ProductMainSerializer(product)
        return Response(serializer.data)

class ProductSectionView(APIView):
    permission_classes = [AllowAny] 

    def get(self, request, name, section):
        logger.info(f"Fetching {section} for product: {name}")
        product = get_object_or_404(Product, name=name)

        if section == "updates":
            updates = product.updates.all()
            serializer = ProductUpdateSerializer(updates, many=True)
            return Response(serializer.data)
        elif section == "version-history":
            version_history = product.version_history.all()
            serializer = VersionHistorySerializer(version_history, many=True)
            return Response(serializer.data)
        else:
            logger.warning(f"Invalid section requested: {section}")
            return Response({"detail": "Invalid section"}, status=400)

class ProductDownloadView(APIView):
    permission_classes = [AllowAny] 

    def post(self, request, name):
        logger.info(f"Incrementing downloads for product: {name}")
        product = get_object_or_404(Product, name=name)
        product.increase_downloads()
        logger.info(f"New download count for {name}: {product.downloads}")
        return Response({"downloads": product.downloads})

class ProductListView(APIView):
    def get(self, request):
        category = request.query_params.get('category', None)
        if category:
            products = Product.objects.filter(category=category)
        else:
            products = Product.objects.all()
        serializer = ProductMainSerializer(products, many=True)
        return Response(serializer.data)

class ProductDetailView(APIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    lookup_field = 'name'
