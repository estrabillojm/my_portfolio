from django.contrib import admin
from django.urls import path, include
from content import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.content_index),
    path('home/', include('content.urls')),
    path('admin-panel/', include('administrator.urls')),
]

urlpatterns += staticfiles_urlpatterns()