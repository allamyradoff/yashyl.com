from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

# from accounts.models import Account, UserProfiles
from accounts.models import *

class AccountSerializerLogin(serializers.ModelSerializer):
	class Meta:
		model = Account
		fields = "__all__"


		
class UserProfilesSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserProfile
		fields = "__all__"

class AccountSerializer(serializers.ModelSerializer):
	isAdmin = serializers.SerializerMethodField(read_only=True)
	user_account = UserProfilesSerializer(many=False, read_only=True)
	class Meta:
		model = Account
		fields = ['id', 'first_name', 'last_name', 'username', 'email', 'phone_number', 'is_admin']

	def get_isAdmin(self, obj):
		return obj.is_staff

class AccountSerializerWithToken(AccountSerializer):
	token = serializers.SerializerMethodField(read_only=True)
	class Meta:
		model = Account
		fields = ['id', 'phone_number', 'email', 'username', 'isAdmin', 'token']

	def get_token(self, obj):
		token = RefreshToken.for_user(obj)
		return str(token.access_token)