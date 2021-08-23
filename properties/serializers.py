from standards.serializers import NoNullSerializer
from rest_framework import serializers
# from properties.models import Like

class PropertySerializer(NoNullSerializer):
   """Serializer representing the property model"""
   address = serializers.CharField(trim_whitespace=True, allow_null=False)
   city = serializers.CharField(trim_whitespace=True, allow_null=False)
   # state = serializers.CharField(trim_whitespace=True, allow_null=False)
   price = serializers.IntegerField(min_value=0, allow_null=False)
   description = serializers.CharField(trim_whitespace=True, allow_blank=True, allow_null=True)

# class LikeSerializer(NoNullSerializer):
#    """Serializer representing the like properties relationship model"""
#    property = PropertySerializer(many=False, read_only=True)

#    def create(self, validated_data):
#         """
#         Create a new like property for a user
#         """
#         try:
#             user = self.context["user"]

#             # Increase likes on related property             
#             property.likes += 1
#             property.save()
#             return Like.objects.create(property=property, user=user)
#         except Exception:
#             raise
