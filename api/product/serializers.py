from rest_framework import serializers
from product.models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


    


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = "__all__"


class CategoryProductsSerializer(serializers.ModelSerializer):
    category_products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = "__all__"


class ProductDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)


    class Meta:
        model = Product
        fields = '__all__'

class LikeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeProduct
        fields = '__all__'