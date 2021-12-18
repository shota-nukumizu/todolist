from django.contrib import admin
from django.urls import path, include

from _app.views import TaskViewSet

from rest_framework import routers

routers = routers.DefaultRouter()
routers.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', include(routers.urls)),
    path('admin/', admin.site.urls),
]
