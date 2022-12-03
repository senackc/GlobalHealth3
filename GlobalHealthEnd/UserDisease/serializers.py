#Controller
from .models import UserDiseaseClass
from rest_framework import serializers

class LoginController(serializers.ModelSerializer):
    class Meta:
        model = UserDiseaseClass #model ismi importu
        fields = "_all_" # örn. UserAllergenClass  ['aa', 'bb', 'cc']