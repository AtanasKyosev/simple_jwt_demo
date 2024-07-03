from django.shortcuts import render

from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer, UserListSerializer
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import UserData


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class UserListView(generics.ListAPIView):
    queryset = UserData.objects.all()
    serializer_class = UserListSerializer
    permission_classes = [IsAuthenticated]
