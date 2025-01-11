# FenixenForge_db/urls.py
from django.urls import path
from .views import ProductListView, ProductMainView, ProductSectionView, ProductDownloadView

urlpatterns = [
    path('data/', ProductListView.as_view(), name='product-list'),
    path('data/<str:name>/', ProductMainView.as_view(), name='product-detail'),
    path('data/<str:name>/download/', ProductDownloadView.as_view(), name='product-download'),
    path('data/<str:name>/<str:section>/', ProductSectionView.as_view(), name='product-section'),
]
