from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from .models import Registration

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = ('event',)