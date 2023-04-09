from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from .serializers import RegistrationSerializer
from .models import Registration


class RegisterEventView(APIView):
    serializer_class = RegistrationSerializer
    queryset = Registration.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = []

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            event = serializer.validated_data['event']
            user = request.user
            registered = Registration.objects.filter(user=user, event=event)
            if not registered:
                Registration.objects.create(event=event, user=user)
                return Response({'data':'User registered for Event'}, status=HTTP_200_OK)
            return Response({'data':'User already registered for Event'}, status=HTTP_200_OK)