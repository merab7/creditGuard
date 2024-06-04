from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import CardViewSet

router = routers.SimpleRouter()
router.register('cards', CardViewSet, basename='cards')

urlpatterns = [
      path('', include(router.urls)),
] 
