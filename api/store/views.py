from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework import generics, status, viewsets, mixins
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.parsers import FileUploadParser
from rest_framework.parsers import MultiPartParser, FormParser

from store.models import *
from .serializers import *
from accounts.models import Account
from rest_framework.pagination import LimitOffsetPagination


@api_view(['GET'])
def storeList(request):
    store = Store.objects.all()
    serializer = StoreSerializer(store, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(['GET'])
def storeDetailList(request, id):
    store = Store.objects.filter(id=id).last()
    # print(store)
    product= StoreProduct.objects.filter(store=store.id)
    # print(product)
    serializer = StoreProductSerializer(product, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)