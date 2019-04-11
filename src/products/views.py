from rest_framework import serializers, viewsets
from rest_framework.generics import CreateAPIView

from products.models import Product, Variant


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        depth = 1
        model = Product
        fields = ('id', 'url', 'store', 'name', 'description', 'slug', 'variant_set')


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        slug = self.request.query_params.get('slug', None)
        if slug is not None:
            queryset = queryset.filter(slug=slug)
        return queryset


class VariantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        depth = 1
        model = Variant
        fields = ('id', 'url', 'product', 'name', 'price', 'image')


class VariantViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = VariantSerializer

    def get_queryset(self):
        queryset = Variant.objects.all()
        slug = self.request.query_params.get('slug', None)
        if slug is not None:
            queryset = queryset.filter(product__slug=slug)
        return queryset


class ProductCreateViewSet(CreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class VariantCreateViewSet(CreateAPIView):
    serializer_class = VariantSerializer
    queryset = Variant.objects.all()
