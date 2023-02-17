from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.hashers import make_password
from rest_framework import generics, status, viewsets, mixins
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from banner.models import *
from .serializers import *


@api_view(['GET'])
def sliderList(request):
    slider = Slider.objects.all()
    serializer = SliderSerializer(slider, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(['GET'])
def topProductList(request):
    top_p = TopProduct.objects.all()
    serializer = TopProductSerializer(top_p, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def topMiniSliderList(request):
    top_mini_slider = MiniSlider.objects.all()
    serializer = MiniSliderSerializer(top_mini_slider, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(['GET'])
def bannerForCharityList(request):
    banner = BannerForCharity.objects.all()
    serializer = BannerForCharitySerializer(banner, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
