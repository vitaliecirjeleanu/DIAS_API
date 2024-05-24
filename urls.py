"""
URL configuration for api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve

from utils.image_upload import ImageUploadView
from utils.image_delete import ImageDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/topics/', include('topics.urls')),
    path('api/int-football/', include('int_football.urls')),
    path('api/image-upload/', ImageUploadView.as_view(), name="image-upload"),
    path('api/image-delete/', ImageDeleteView.as_view(), name="image-delete")
]

urlpatterns += [ re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})] 