from standards.serializers import NoNullSerializer
from rest_framework import serializers
# from properties.models import Favorite

class PropertySerializer(NoNullSerializer):
   """Serializer representing the property model"""
   address = serializers.CharField(trim_whitespace=True, allow_null=False)
   city = serializers.CharField(trim_whitespace=True, allow_null=False)
   # state = serializers.CharField(trim_whitespace=True, allow_null=False)
   price = serializers.IntegerField(min_value=0, allow_null=False)
   description = serializers.CharField(trim_whitespace=True, allow_blank=True, allow_null=True)

# class FavoriteSerializer(NoNullSerializer):
#    """Serializer representing the favorite properties relationship model"""
#    property = PropertySerializer(many=False, read_only=True)

#    def create(self, validated_data):
#         """
#         Create a new favorite property for a user
#         """
#         try:
#             user = self.context["user"]
#             return Favorite.objects.create(property=validated_data.get("property"), user=user)
#         except Exception:
#             raise
