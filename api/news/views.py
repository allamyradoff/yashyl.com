from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework import generics, status, viewsets, mixins
from django.shortcuts import redirect, render, get_object_or_404
from store.models import *
from .serializers import *
from django.contrib import messages, auth
from accounts.models import Account
from rest_framework.pagination import LimitOffsetPagination



@api_view(['GET'])
def newsList(request):
    news = News.objects.all()
    serializer = NewsSerializer(news, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)




@api_view(['GET'])
def newsDetailList(request, id):
    news = News.objects.filter(id=id)    
    serializer = NewsSerializer(news, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


