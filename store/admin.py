from django.contrib import admin
from .models import *

class StoreProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'store', 'price')


admin.site.register(Store)
admin.site.register(StoreProduct, StoreProductAdmin)
