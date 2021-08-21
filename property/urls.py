from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from property import views

urlpatterns = [
    url(r"^$", views.ApiProperty.as_view(), name="property detail")
]

urlpatterns = format_suffix_patterns(urlpatterns)
