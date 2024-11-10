from rest_framework import serializers
from .models import Machine, ErrorCode, ErrorProtocol

class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = '__all__'

class ErrorCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ErrorCode
        fields = '__all__'

class ErrorProtocolSerializer(serializers.ModelSerializer):
    class Meta:
        model = ErrorProtocol
        fields = '__all__'