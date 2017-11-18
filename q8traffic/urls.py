"""q8traffic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from main import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^create_ticket/$', views.create_ticket, name='create_ticket'),
    url(r'^list/$', views.ticket_list, name='list'),
    url(r'^about/$', views.about, name='about'),
    url(r'^violation_list/$', views.violation_list, name='violation_list'),
    url(r'^login/$', views.mylogin, name='login'),
    url(r'^logout/$', views.mylogout, name='logout'),
    url(r'^/$', views.ticket_list),
    url(r'^$', views.ticket_list),


]
