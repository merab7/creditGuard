from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('cards/', include('cards.urls')),
    path('', include('cards.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]
