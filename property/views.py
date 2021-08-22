import re

from property.entities import EntityProperty
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from standards.responses import StandardResponse

# Create your views here.
class ApiProperty(APIView):
    permission_classes = (permissions.AllowAny,)
    response = StandardResponse

    def get(self, request):
        """GET endpoint
        Retrieve a list of properties given some filters via query params
        valid query params: [city, state, min_year, max_year]

        Args:
            request (HttpRequest): Request sent by user|FrontEnd

        Returns:
            HttpResponse: List of properties 
        """

        params = {
            "city": '',
            "state": '',
            "min_year": 0,
            "max_year": 0
        }

        try:
            self.get_params(request=request, params=params)
            properties = EntityProperty.get_list(city=params['city'], state=params['state'], min_year=params['min_year'], max_year=params['max_year'])
            return self.response.send_200(data=properties)

        except Exception as e:
            print(e)
            return self.response.send_500()

    def get_params(self, request, params):
        """Process all query params on request

        Args:
            request (HttpRequest): Request
            params (dict): params to process
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