from utils.mysql_utils import Database
from django.conf import settings
from property.serializers import PropertySerializer

database = Database(
    host=settings.DATABASES['default']['HOST'],
    port=settings.DATABASES['default']['PORT'],
    user=settings.DATABASES['default']['USER'],
    password=settings.DATABASES['default']['PASSWORD'],
    database=settings.DATABASES['default']['NAME']
)

class EntityProperty:

    def get_list():
        try:
            return []
            serializer = PropertySerializer(query_result, many=True)
            return serializer.data
        except Exception:
            raise