"""DLRanking URL Configuration

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
from django.conf.urls import url
from django.contrib import admin

from django.conf.urls.static import static
from django.conf import settings

from allframe import views


urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url('^$', views.index),
    url(r'^index/', views.index),
    url(r'^frameinfo/', views.frameinfo),
    url(r'^real/', views.real),
    url(r'^star/', views.star),
    url(r'^fork/', views.fork),
    url(r'^watch/', views.watch),
    url(r'^star_graph/', views.star_graph),
    url(r'^fork_graph/', views.fork_graph),
    url(r'^watch_graph/', views.watch_graph),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
