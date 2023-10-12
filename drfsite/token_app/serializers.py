from rest_framework import serializers
from .models import Token


class WomenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ('token')