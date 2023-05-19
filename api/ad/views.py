from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.hashers import make_password
from rest_framework import generics, status, viewsets, mixins
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from obyawleniya.models import *
from .serializers import *
from news.models import *

from rest_framework.pagination import LimitOffsetPagination


# @api_view(['GET'])

class AdListView(APIView, LimitOffsetPagination):
    def get(self, request):
        # permission_classes = [IsAuthenticated]
        ad = Ad.objects.all()
        # serializer = AdSerializer(ad, many=True)
        results = self.paginate_queryset(ad,  request, view=self)
        serializer = AdSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)
        # return Response(serializer.data, status=status.HTTP_200_OK)


class AdCreateView(generics.CreateAPIView, generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Ad.objects.all()
    serializer_class = AdCreateSerializer


class AdsDelete(APIView):
    # permission_classes = [IsAuthenticated]
    def delete(self, request, pk):
        try:
            ad = Ad.objects.get(pk=pk)
            ad.delete()
            return Response({"response": "Удачно"}, status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({"response": "Ошибка"}, status=status.HTTP_403_FORBIDDEN)


class AdsDetail(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        try:
            ad = Ad.objects.get(pk=pk)
            print(ad)
            serializer = AdSerializer(ad, many=False)
            return Response({"response": "Удачно", "data": serializer.data}, status=status.HTTP_200_OK)
        except:
            return Response({"response": "Ошибка"}, status=status.HTTP_403_FORBIDDEN)


class LastAds(APIView):
    def get(self, request):
        try:
            ad = Ad.objects.all().order_by('-id')[:5]
            serializer = AdSerializer(ad, many=True)
            return Response({"response": "Удачно", "data": serializer.data}, status=status.HTTP_200_OK)
        except:
            return Response({"response": "Ошибка"}, status=status.HTTP_403_FORBIDDEN)
