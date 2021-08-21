import re

from property.entities import EntityProperty
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from django.http import JsonResponse
from rest_framework import status

# Create your views here.
class ApiProperty(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        """[summary]

        Args:
            request ([type]): [description]

        Returns:
            [type]: [description]
        """

        params = {
            "city": '',
            "state": '',
            "min_year": 0,
            "max_year": 0
        }

        try:
            self.get_params(request=request, params=params)
            response = EntityProperty.get_list()
            return Response(response, status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            return Response({"error": "error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get_params(self, request, params):
        """[summary]

        Args:
            request ([type]): [description]
            params ([type]): [description]
        """
        for key in params.items():
            if request.GET.get(key[0]):
                # Normalize params
                value = request.GET[key[0]].strip()
                value = re.sub(" +", " ", value)

                # If key is year, convert to integer
                if key[0] == 'min_year' or key[0] == 'max_year':
                    try:
                        value = int(value)
                    except ValueError:
                        value = 0
                
                # Update value if exists
                params[key[0]] = value