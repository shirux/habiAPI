from standards.serializers import NoNullSerializer
from rest_framework import serializers

class PropertySerializer(NoNullSerializer):
   """Your data serializer, define your fields here."""
   address = serializers.CharField(trim_whitespace=True)
   city = serializers.CharField(trim_whitespace=True)
   # state = serializers.CharField(trim_whitespace=True)
   price = serializers.IntegerField(min_value=0)
   description = serializers.CharField(trim_whitespace=True, allow_blank=True)