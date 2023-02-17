from rest_framework import serializers
from orders.models import *



class UserOrderSerializer(serializers.ModelSerializer):
	class Meta:
		model = Order
		fields = "__all__"


class OrderItemsSerializer(serializers.ModelSerializer):
	class Meta:
		model = OrderProduct
		fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'



class OrderItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = '__all__'