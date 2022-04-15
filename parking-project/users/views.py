from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from rest_framework.response import Response
from .models import CustomUser
from rest_framework import generics, status
from .serializers import CustomUserSerializer
import json
import requests
from rest_auth.views import LoginView
from rest_framework.views import APIView
from django.conf import settings
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
# Create your views here.


class CustomUserUpdate(generics.RetrieveUpdateAPIView):
	# API endpoint that allows a customer record to be updated.
	queryset = CustomUser.objects.all()
	serializer_class = CustomUserSerializer

	def update(self, request, *args, **kwargs):
		partial = kwargs.pop('partial', False)
		instance = get_object_or_404(CustomUser, id = request.user.id)
		serializer = self.get_serializer(instance, data=request.data, partial=partial)
		serializer.is_valid(raise_exception=True)
		self.perform_update(serializer)

		if getattr(instance, '_prefetched_objects_cache', None):
			# If 'prefetch_related' has been applied to a queryset, we need to
			# forcibly invalidate the prefetch cache on the instance.
			instance._prefetched_objects_cache = {}

		return Response(serializer.data)

#Return user Role by token
class UserRole(generics.RetrieveAPIView):
	def get(self, request, *args, **kwargs):
		user = get_object_or_404(CustomUser, auth_token = request.auth)
		serializer=CustomUserSerializer(user)
		return Response(serializer.data['role'])
		
#Return user role alongside with token 
class CustomLoginView(LoginView):
	def get_response(self):
		data = {
				'role': self.user.role,
			}
		orginal_response = super().get_response()
		orginal_response.data.update(data)
		return orginal_response

class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter
class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter

class SmsTestView(APIView):
	authentication_classes = [] 
	permission_classes = [] 

	def post(self, request, *args, **kwargs):
		number=request.data['number']
		data = {'from': '50004001885294', 'to': number, 'text': 'پیام تست'}
		response = requests.post('https://console.melipayamak.com/api/send/simple/7557787143184d838512628417a5001f', json=data)
		return Response(response, status=status.HTTP_200_OK)