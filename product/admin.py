from django.contrib import admin
from . models import *
from django.utils.html import format_html

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'name')
    list_editable = ('name',)



class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('image_tag', 'name', 'price', 'stock', 'created_date', 'is_active', 'is_sale', 'is_new', 'is_store', 'category', 'cource_price')
    list_editable = ('cource_price',)

    def image_tag(self,obj):
        return format_html('<img src="{0}" style="width: 100px; height:100px;" />'.format(obj.image.url))


class VariationAdmin(admin.ModelAdmin):

    list_display = ( 'variation_value', 'variation_category', 'created_date', 'is_active', )
    list_editable = ('is_active',)
    list_filter = ( 'variation_value', 'variation_category',)



admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, VariationAdmin)
admin.site.register(ReviewRating)
admin.site.register(Cours)
admin.site.register(Brand)
admin.site.register(SubCategory)
admin.site.register(LikeProduct)


