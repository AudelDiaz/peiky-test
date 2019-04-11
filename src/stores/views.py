from django.contrib.auth.models import User
from rest_framework import serializers, viewsets

from stores.models import Store


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username')


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(username=self.request.user.username)


class StoreSerializer(serializers.HyperlinkedModelSerializer):
    user_details = UserSerializer(source='user', read_only=True)

    class Meta:
        depth = 1
        model = Store
        fields = ('id', 'url', 'name', 'slogan', 'logo', 'slug', 'user_details', 'product_set')


class StoreViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = StoreSerializer

    def get_queryset(self):
        queryset = Store.objects.all()
        slug = self.request.query_params.get('slug', None)
        if slug is not None:
            queryset = queryset.filter(slug=slug)
        return queryset
