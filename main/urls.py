from django.urls import include, path
from rest_framework import routers
from .views import DocumentViewSet

router = routers.DefaultRouter()
router.register(r'documents', DocumentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
