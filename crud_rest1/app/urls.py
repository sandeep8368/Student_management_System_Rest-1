from django.urls import path,include
from rest_framework.routers import DefaultRouter
from app.views import studentViewSet


router = DefaultRouter()

router.register(r'api',studentViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
