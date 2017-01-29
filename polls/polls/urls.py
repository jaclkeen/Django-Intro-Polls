"""polls URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# namespace is used to specify which module a particular view belongs to. Is used on links in templates
from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^polls/', include('pollsMod.urls', namespace="polls")),
    url(r'^admin/', admin.site.urls),
    url(r'^login', views.login, name='login'),
    url(r'^logout', views.logout, name='logout'),
    url(r'^createUser', views.createNewUser, name='createUser'),
    url(r'^', views.index, name='register'),    
]
