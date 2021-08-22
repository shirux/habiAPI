from django.conf import settings
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response


class StandardResponse:

    @staticmethod
    def send_200(data):
        """Return a JSON on a Response with a 200 status

        Args:
            data (dict|Array): Data to be sent on response

        Returns:
            Response: Response with a message on a JSON
        """
        response = {
            "data": data
        }

        return Response(response, status=status.HTTP_200_OK)

    @staticmethod
    def send_500():
        """Return a Response with a 500 status

        Returns:
            Response: Response with a message on a JSON
        """
        response = {
            "error": "Sorry, We could not process your request. Try later"
        }

        return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)