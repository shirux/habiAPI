from utils.mysql_utils import Database
from django.conf import settings
from properties.serializers import PropertySerializer
# from properties.serializers import FavoriteSerializer

database = Database(
    host=settings.DATABASES['default']['HOST'],
    port=settings.DATABASES['default']['PORT'],
    user=settings.DATABASES['default']['USER'],
    password=settings.DATABASES['default']['PASSWORD'],
    database=settings.DATABASES['default']['NAME']
)

class PropertyEntity:

    @staticmethod
    def get_list(city='', state='', min_year=0, max_year=0):
        """Create a dynamic query to retrieve list of properties 
        with its last status update.
        Can apply filters to result. Valid filters are:
            - city: City name
            - state: State name
            - min_year: Minimum year
            - max_year: Maximum year
        
        Args:
            city (str, optional): City name to filter. Appends to query if its truthy. Defaults to ''.
            state (str, optional): State name to filter. Appends to query if its truthy. Defaults to ''.
            min_year (int, optional): Minimum year. Appends to query if its truthy. Defaults to 0.
            max_year (int, optional): Maximum year. Appends to query if its truthy. Defaults to 0.

        Returns:
            dict: Serialized properties data
        """
        
        try:
            query = """
                SELECT C.address, C.city, C.price, C.description FROM status_history A
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

            # Execute query and serialize result
            query_result = database.query(query)
            serializer = PropertySerializer(query_result, many=True)
            return serializer.data
        except Exception:
            raise

# class FavoriteEntity:

#     @staticmethod
#     def set_property_favorite(user, property_id):
#         """Create or remove a favorite property from a user
        
#         Args:
#             user (User): City name to filter.
#             property_id (int): Property Id.
#         """
#         try:

#             # We append the respective query on database
#             # query = f"""
#             # SELECT * FROM favorites 
#             # WHERE user_id = {user.pk}
#             # AND property_id = {property_id}
#             # """

#             # This one is done via ORM
#             favorite = Favorite.objects.filter(property=property_id, user=user.pk).first()

#             # If relationship exists, then user is removing one favorite
#             if favorite:
#                 favorite.detele()
#             # Otherwise, user selects a new property as favorite
#             else:
#                 context = {"user": user}
#                 serializer = FavoriteSerializer(data={}, context=context, many=False)
#                 if serializer.is_valid(raise_exception=True):
#                     serializer.save()

#         except Exception:
#             raise