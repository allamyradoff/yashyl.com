from rest_framework import serializers
from news.models import *


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'banner_mobile', 'title_mobile', 'desc_mobile']
