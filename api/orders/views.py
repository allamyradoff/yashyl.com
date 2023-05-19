from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework import generics, status, viewsets, mixins
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.parsers import FileUploadParser
from rest_framework.parsers import MultiPartParser, FormParser

from orders.models import *
from .serializers import *
from accounts.models import Account


class UserOrderView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        orders = Order.objects.all().order_by('-created_at')
        serializer = UserOrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Что-то пошло не так. Если повторится, обратитесь к системному администратору.'}, status=status.HTTP_400_BAD_REQUEST)


class UserOrderList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            user_orders = Order.objects.filter(user__id=request.user.id)
            serializer = UserOrderSerializer(user_orders, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({'error': 'Вы не авторизованы для данного типа действий'}, status=status.HTTP_400_BAD_REQUEST)



class OrderCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user.id
        data = request.data
        data['user'] = user
        items = data['items']
        items_total = 0
        if len(items) > 0:
            for item in items:
                items_total += float(item['price']) * float(item['quantity'])
        data['order_total'] = items_total
        serializer = UserOrderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            for item in items:
                item['order'] = serializer.data['id']
                item_serializer = OrderItemCreateSerializer(data=item)
                if item_serializer.is_valid():
                    item_serializer.save()
                else:
                    return Response({"response": "error", "message": item_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'response': 'success', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"response": "error", "message": "Something wrong in request body."})


class OrderItemsDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        try:
            order = Order.objects.get(id=id)
            print(order)
            order_p = OrderProduct.objects.filter(order_id=order)
            print(order_p)
            serializer = OrderItemsSerializer(order_p, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({'error': 'Что-то пошло не так.'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        try:
            order = OrderProduct.objects.get(id=id)
            serializer = OrderItemsSerializer(order, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'error': 'Что-то пошло не так..'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id):
        try:
            order = OrderProduct.objects.get(id=id)
            order.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({'error': 'Что-то пошло не так..'}, status=status.HTTP_404_NOT_FOUND)

