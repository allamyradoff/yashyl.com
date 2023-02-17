from rest_framework import serializers
from obyawleniya.models import *


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = "__all__"


class AdCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Ad
        fields = '__all__'

    def create(self, validated_data):
    	return Ad.objects.create(**validated_data)
