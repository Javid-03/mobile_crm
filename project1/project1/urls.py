"""
URL configuration for project1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from mobile.views import Viewmobile,Listmobile,Detailsmobile,Updatemobile,Deletemobile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Listmobile.as_view(),name="mob-all"),
    path('<int:pk>',Detailsmobile.as_view(),name="mob-view"),
    path('<int:pk>/update',Updatemobile.as_view(),name="mob-edit"),
    path('<int:pk>/delete',Deletemobile.as_view(),name="mob-del"),
    path('add/',Viewmobile.as_view(),name="mob-add"),
]
