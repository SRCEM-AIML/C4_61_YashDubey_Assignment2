# StudentProject/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('first.urls')),   # Routes to first app
    path('second/', include('second.urls')),  # Routes to second app
]
