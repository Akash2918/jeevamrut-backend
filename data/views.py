from django.shortcuts import render

# Create your views here.
from .models import Data
from rest_framework.views import APIView
from .serializers import DataSerializer
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


class DataViewSet(APIView):

    permission_classes = [AllowAny]

    def post(self, request, format=None):
        print(request)
        serializer = DataSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
        
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        
        serializer = DataSerializer(Data.objects.all().order_by('-id'), many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)





