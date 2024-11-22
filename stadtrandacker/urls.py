from django.urls import path, include
from django.contrib import admin
import juntagrico

urlpatterns = [
    path('admin/', admin.site.urls),
    path('impersonate/', include('impersonate.urls')),
    path('', include('juntagrico.urls')),
]
