from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response


class StandardResponse:

    @staticmethod
    def not_found(request, path=""):
        """Route not found

        Returns:
            Response: Response with a default message and 404 bad request
        """
        return JsonResponse({"Error": "The resource was not found"}, status=status.HTTP_404_NOT_FOUND)

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
    def send_204():
        """Return a Response with a 204 NO CONTENT status

        Returns:
            Response: Bodyless response
        """

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    @staticmethod
    def send_404(instance="Object"):
        """Return a Response with a 404 NOT FOUND status.
        Message is dynamic with the instance|object not found

        Args:
            instance (str, optional): Entity|Object|Instance the user was searching for. Defaults to "Object".

        Returns:
            Response: Response with a message on a JSON
        """

        response = {
            "error": str(instance) + " not found."
        }
        return Response(response, status=status.HTTP_404_NOT_FOUND)

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