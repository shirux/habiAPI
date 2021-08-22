from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from properties import views

urlpatterns = [
    url(r"^$", views.PropertiesApi.as_view(), name="properties")
]

urlpatterns = format_suffix_patterns(urlpatterns)
