from django.conf.urls import url

from .views import first_api_view

urlpatterns = [
    url('first', first_api_view),
]
