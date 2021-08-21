from django.http import JsonResponse
from django.urls import path
from django.conf.urls import url
from django.urls import include
from rest_framework import status

# 404
def error404(request, path=""):
    return JsonResponse({"Error": "The resource was not found"}, status=status.HTTP_400_BAD_REQUEST)

urlpatterns = [
    url(r"^$", error404),
    path("api/property", include("property.urls")),
    url(r"^(?P<path>.*)/$", error404),
]
