from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import RegisterSerializer
# Create your views here.

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = {}
        data['response'] = 'successfully registered a new user'
        data['reg_no'] = user.reg_no
        data['name'] = user.name
        data['email'] = user.email
        data['dept'] = user.dept
        data['domain'] = user.domain
        return Response(data)