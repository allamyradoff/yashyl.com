from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework import generics, status, viewsets, mixins
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.parsers import FileUploadParser
from rest_framework.parsers import MultiPartParser, FormParser

from product.models import Product, Category
from .serializers import *
from accounts.models import Account
from rest_framework.pagination import LimitOffsetPagination


class ProductListView(APIView, LimitOffsetPagination):
    def get(self, request):
        try:
            name = None
            category_id = None
            is_sale = None
            is_new = None
            priority_sale = None
            priority_chosen = None
            minPrice = None

            products = Product.objects.filter(is_active=True)
            if request.query_params.get('name', None):
                name = request.query_params.get('name', None)
                products = products.filter(name__icontains=name)
            if request.query_params.get('category_id', None):
                category_id = request.query_params.get('category_id', None)
                products = products.filter(category_id=category_id)
                print(products)

            if request.query_params.get('is_sale', None):
                is_sale = request.query_params.get('is_sale', None)
                products = products.filter(is_sale=is_sale)

            if request.query_params.get('is_new', None):
                is_new = request.query_params.get('is_new', None)
                products = products.filter(is_new=is_new)
            if request.query_params.get('priority_chosen', None):
                priority = request.query_params.get('priority_chosen', None)
                products = products.filter(priority__icontains='CHOSEN')
            if request.query_params.get('minPrice', None):
                minPrice = request.query_params.get('minPrice', None)
                if minPrice == '0':
                    products = products.order_by('cource_price')
                elif minPrice > '0':
                    products = products.order_by('-cource_price')
            # serializer = ProductSerializer(products, many=True)
            # return Response(serializer.data)
            results = self.paginate_queryset(products,  request, view=self)
            serializer = ProductSerializer(results, many=True)
            return self.get_paginated_response(serializer.data)
        except:
            message = {'detail': 'None'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def categoryList(request):
    category = Category.objects.all()
    serializer = CategorySerializer(category, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


class CategoryProductsView(APIView):
    def get(self, request, pk):
        title = None

        try:
            category_products = Category.objects.get(pk=pk)
            products = Product.objects.filter(category_id=category_products)

            if request.query_params.get('title', None):
                title = request.query_params.get('title', None)
                products = products.filter(name__icontains=title)

            serializer = CategoryProductsSerializer(products, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)


class ProductDetailView(APIView):
    def get(self, request, pk):
        try:
            product = Product.objects.get(id=pk)
            if not product:
                return Response(None)
            serializer = ProductDetailSerializer(product)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def likeGetProduct(request):
    permission_classes = [IsAuthenticated]
    data = request.data
    user = request.user

    try:
        like = LikeProduct.objects.filter(user=user)
        serializers = LikeCreateSerializer(like, many=True)
        return Response(serializers.data)
    except:
        return Response({'error':'?? ?????? ???????? ?????????????? ?????????????? ?????? ??????????????????????'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def likeProduct(request):
    permission_classes = [IsAuthenticated]
    data = request.data
    try:
        p_like = LikeProduct.objects.create(
            user_id=request.user.id,
            product_id=data['product_id'],
        )
        serializer = LikeCreateSerializer(p_like, many=False)
        return Response(serializer.data)
    except:
            return Response({'error': '???????? ?????? ?????????????????? ???? ???????? ??????????????'}, status=status.HTTP_404_NOT_FOUND)


class LikeProductDelete(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self, request, pk):
        try:
            p_like = LikeProduct.objects.get(pk=pk)
            p_like.delete()
            return Response({"response": "????????????"}, status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({"response": "????????????"}, status=status.HTTP_403_FORBIDDEN)




