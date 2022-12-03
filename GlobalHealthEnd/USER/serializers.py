
from django.contrib.auth import authenticate
from rest_framework import serializers
from django.utils.translation import gettext as _


class UserLoginSerializer(serializers.Serializer):
    IdentificicationNumber = serializers.CharField(max_length=20)
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        IdentificicationNumber = data.get("IdentificicationNumber")
        password = data.get("password")

        if IdentificicationNumber and password:
            user = authenticate(
                request=self.context.get("request"), username=IdentificicationNumber, password=password
            )

            if not user:
                msg = _("Unable to log in with provided credentials.")
                raise serializers.ValidationError(msg, code="authorization")

        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code="authorization")

        data["user"] = user
        return data