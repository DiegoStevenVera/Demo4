from django.conf.urls import url
from django.contrib import admin
from django.urls import include
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('user.urls')),
    path('api/v1/', include('administrator.urls')),
    url(r'^api-auth/', include('rest_framework.urls')),
]
