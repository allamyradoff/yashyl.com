from rest_framework import serializers
from banner.models import *


class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = "__all__"


class TopProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopProduct
        fields = "__all__"


class MiniSliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = MiniSlider
        fields = "__all__"




class BannerForCharitySerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerForCharity
        fields = "__all__"
