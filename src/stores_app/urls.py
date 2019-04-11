"""stores_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from rest_framework import routers

from products.views import ProductViewSet, VariantViewSet, ProductCreateViewSet, VariantCreateViewSet
from stores.views import StoreViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet, base_name='product')
router.register(r'variants', VariantViewSet, base_name='variant')
router.register(r'stores', StoreViewSet, base_name='store')
router.register(r'users', UserViewSet, base_name='user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/admin/products/create/', ProductCreateViewSet.as_view(), name='product-create'),
path('api/admin/variants/create/', VariantCreateViewSet.as_view(), name='variant-create'),
    url(r'^api-auth/', include('rest_framework.urls'))
]
