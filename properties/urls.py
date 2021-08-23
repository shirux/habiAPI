from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from properties import views
from standards.responses import StandardResponse

urlpatterns = [
    url(r"^$", views.PropertiesApi.as_view(), name="properties"),
    # url(r"^likes/(?P<property_id>\d+)/$", views.LikesApi.as_view(), name="like properties"),
    url(r"^(?P<path>.*)/$", StandardResponse.not_found),
]

urlpatterns = format_suffix_patterns(urlpatterns)
