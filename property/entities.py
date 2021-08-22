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

    def get_list(city='', state='', min_year=0, max_year=0):
        try:
            query = """
                SELECT C.address, C.city, C.price, C.year, C.description from status_history A
                JOIN status B ON B.id = A.status_id
                JOIN property C ON C.id = A.property_id
                WHERE (A.property_id, A.update_date) IN (select  property_id, max(update_date) AS update_date from status_history GROUP BY property_id)
                AND (B.name = 'pre_venta' OR B.name = 'en_venta' OR B.name = 'vendido')
            """

            # Apply filters
            if city:
                query = f"{query} AND city = '{city}'"
            # if state:
            #     query = f"{query} AND state = '{state}'"
            if min_year:
                query = f"{query} AND year >= {min_year}"
            if max_year: 
                query = f"{query} AND year <= {max_year}"

            print(query)
            query_result = database.query(query)
            serializer = PropertySerializer(query_result, many=True)
            return serializer.data
        except Exception:
            raise