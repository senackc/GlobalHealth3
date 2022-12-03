#Controller
from .models import UserAllergenClass
from rest_framework import serializers

class LoginController(serializers.ModelSerializer):
    class Meta:
        model = UserAllergenClass #model ismi importu
        fields = "_all_" # örn. UserAllergenClass  ['aa', 'bb', 'cc']