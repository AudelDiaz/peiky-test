from django.contrib import admin

from stores.models import Store


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    pass
