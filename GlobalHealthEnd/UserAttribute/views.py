from django.shortcuts import render
from rest_framework import generics,status
# Create your views here.
from rest_framework.response import Response
from .models import UserAttribute
from .serializer import AttributeInformationsDetailsSerializer

import uuid

class AttributeSaveView(generics.ListAPIView): 

    def get(self, request, *args, **kwargs):
   
        attribute = AttributeInformations.objects.all().order_by('-recieved_date')[:5] # model ismi =den sonra 
        #tmp = modelismi.objects.Create(**request.data)
        serializer = AttributeInformationsDetailsSerializer(attribute,many = True)
        
        
        return Response({"Message": "successful","body":serializer.data}, status=status.HTTP_200_OK)


class AttributeCreateView(generics.CreateAPIView): 

    def post(self, request, *args, **kwargs):
   
        queryset = AllergentInformations.objects.all().order_by('-recieved_date')[:5] # model ismi =den sonra 
        #tmp = modelismi.objects.Create(**request.data)
        serializer = AllergenInformationsDetailsSerializer(queryset,many = True)
        
        return Response({"Message": "successful","body":serializer.data}, status=status.HTTP_200_OK)
     

# CreateAPIView 
# listApiView yerine yukarıdakini yaz def'ten sonra get-posları kullan
