# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include  # add thi

urlpatterns = [
    path('admin/', admin.site.urls),   
    path("", include("apps.authentication.urls")),
    path("", include("apps.home.urls")) ,
    path("", include("apps.user.urls")),
    path("", include("apps.emp.urls")),
] 
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)