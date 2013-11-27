from django.conf.urls import patterns, url, include
from django_ninfo import views

from rest_framework import routers
router = routers.DefaultRouter()

urlpatterns = patterns('',
    url(r'api/', include(router.urls)),
)
