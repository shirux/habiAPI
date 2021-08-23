from django.urls import path
from django.conf.urls import url
from django.urls import include
from standards.responses import StandardResponse

urlpatterns = [
    url(r"^$", StandardResponse.not_found),
    path("api/properties/", include("properties.urls")),
    url(r"^(?P<path>.*)/$", StandardResponse.not_found),
]
