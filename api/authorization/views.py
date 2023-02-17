from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.hashers import make_password
from rest_framework import generics, status, viewsets, mixins
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.parsers import FileUploadParser
from rest_framework.parsers import MultiPartParser, FormParser

from accounts.models import *
from .serializers import UserProfilesSerializer, AccountSerializer, AccountSerializerWithToken


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        serializer = AccountSerializerWithToken(self.user).data
        for k, v in serializer.items():
            data[k] = v
        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['POST'])
def registerUser(request):
    data = request.data
    try:
        user = Account.objects.create(
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email'],
            username=data['email'],
            phone_number=data['phone_number'],
            password=make_password(data['password']),
            is_active=True
        )
        serializer = AccountSerializerWithToken(user, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'Bu nomer bilen ulanyjy eýýäm bar.'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


class AccountProfileView(APIView):

    permission_classes = [IsAuthenticated]

    parser_classes = [MultiPartParser, FormParser, FileUploadParser]


    def get(self, request):
        try:
            user = request.user
            profile = UserProfile.objects.filter(user=user).first()
            serializer = UserProfilesSerializer(profile, many=False)
            return Response({"response":"Удачно", "data":serializer.data}, status=status.HTTP_200_OK)
        except:
            return Response({"response":"Ошибка"}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        try:
            user = request.user
            data = request.data
            data["user"] = user.id

            serializer = UserProfilesSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"response": "Ошибка"}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        try:
            user = request.user
            data = request.data
            data._mutable = True
            data['user'] = user.id
            data._mutable = False
            profile = UserProfile.objects.get(user=user)
            serializer = UserProfilesSerializer(profile, data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({"response": "Удачно", "data": serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({"response": "Ошибка"}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"response": "Ошибка"}, status=status.HTTP_404_NOT_FOUND)


class ProfileDelete(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self, request, pk):
        try:
            profile = UserProfile.objects.get(pk=pk)
            profile.delete()
            return Response({"response": "Удачно"}, status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({"response": "Ошибка"}, status=status.HTTP_403_FORBIDDEN)



