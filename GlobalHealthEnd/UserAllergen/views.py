
from django.shortcuts import render
from rest_framework import generics,status
# Create your views here.
from rest_framework.response import Response
from .models import User
from .serializer import AllergenInformationsDetailsSerializer

import uuid



class AllergenSaveView(generics.ListAPIView): 

    def get(self, request, *args, **kwargs):
   
        allergen = AllergenInformations.objects.all().order_by('-recieved_date')[:5] # model ismi =den sonra 
        #tmp = modelismi.objects.Create(**request.data)
        serializer = AllergenInformationsDetailsSerializer(allergen,many = True)
        
        
        return Response({"Message": "successful","body":serializer.data}, status=status.HTTP_200_OK)


class AllergenCreateView(generics.CreateAPIView): 

    def get(self, request, *args, **kwargs):
   
        newAllergen = AllergentInformations.objects.all().order_by('-recieved_date')[:5] # model ismi =den sonra 
        #tmp = modelismi.objects.Create(**request.data)
        serializer = AllergenInformationsDetailsSerializer(newAllergen,many = True)
        
     

# CreateAPIView 
# listApiView yerine yukarıdakini yaz def'ten sonra get-posları kullan
