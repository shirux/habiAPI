from collections import OrderedDict

from rest_framework import serializers
from rest_framework.fields import SkipField


class NoNullSerializer(serializers.Serializer):
    def to_representation(self, instance):
        """
        Remove nulls from serializers.
        Taken from https://stackoverflow.com/questions/27015931/remove-null-fields-from-django-rest-framework-response

        """
        ret = OrderedDict()
        fields = [field for field in self.fields.values() if not field.write_only]

        for field in fields:
            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue

            if attribute is not None:
                representation = field.to_representation(attribute)
                if representation is None:
                    # Do not seralize empty objects
                    continue
                if isinstance(representation, list) and not representation:
                    # Do not serialize empty lists
                    continue
                ret[field.field_name] = representation

        return ret