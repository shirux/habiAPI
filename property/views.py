from rest_framework.views import APIView
from rest_framework import permissions
from django.http import JsonResponse
from rest_framework import status

# Create your views here.
class ApiProperty(APIView):
    permission_classes = (permissions.AllowAny,)

    VALID_QUERY_PARAMETERS = {

    }

    def get(self, request):

        # Filters
        city = None
        state = None
        min_year = None
        max_year = None

        try:
            return JsonResponse({"message": "holis"}, status=status.HTTP_200_OK)

        except Exception:
            return JsonResponse({"error": "error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    