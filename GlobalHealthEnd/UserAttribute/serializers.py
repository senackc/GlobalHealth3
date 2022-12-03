#Controller
from .models import UserAttributeClass
from rest_framework import serializers

class LoginController(serializers.ModelSerializer):
    class Meta:
        model = UserAttributeClass 
        fields = "_all_"