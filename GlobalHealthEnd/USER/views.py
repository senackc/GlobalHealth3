from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics,status,permissions
from .serializers import UserLoginSerializer

# Create your views here.
class UserLoginView(generics.GenericAPIView):

    serializer_class = UserLoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.get_serializer(
            data=request.data, context={"request": request}
        )
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data["user"]
        
            return Response(
                {
                    "token": str("token"),
                },
                status=status.HTTP_200_OK,
            )
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)