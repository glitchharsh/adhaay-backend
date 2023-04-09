from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from .models import Registration

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = ('event',)

#eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgxMDYzMjQ3LCJpYXQiOjE2ODEwNTk2NDcsImp0aSI6IjJjOWEyODAzZDc3NTQ1NTI5N2E1ZWM5ZWY5ODQyMTc0IiwidXNlcl9pZCI6NSwibmFtZSI6Inh5eiJ9.sB_JIkky7MuHkSEUSKWfTrnI0AffElRq76JqOeOsV-s