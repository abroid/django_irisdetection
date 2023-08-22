from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('detect_iris.urls')),
    path('admin/', admin.site.urls),
]
