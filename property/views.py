from property.entities import EntityProperty
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from standards.responses import StandardResponse
from utils.request_utils import RequestUtils

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

        # Retrieve params and fetch data from database
        try:
            RequestUtils.process_params(request=request, params=params)
            properties = EntityProperty.get_list(city=params['city'], state=params['state'], min_year=params['min_year'], max_year=params['max_year'])
            return self.response.send_200(data=properties)

        # Send 500 Internal Server Error
        except Exception:
            return self.response.send_500()

    