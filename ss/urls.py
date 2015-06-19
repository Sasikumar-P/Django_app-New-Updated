"""ss URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns

from django.contrib import admin
from django.contrib.auth.models import User

from sss import views
from django.conf import settings
from registration.backends.simple.views import RegistrationView




urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^add/$', views.add, name='add'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', views.index, name='new'),
    url(r'^index2/', views.index2, name='new2'),
    url(r'^register/$', views.register, name='register'),
    url(r'^upload/$', views.upload, name='upload'),
    url(r'^family/$', views.family, name='family'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^restricted/', views.restricted, name='restricted'),
    url(r'^logout/$', views.user_logout, name='logout'), # ADD NEW PATTERN!
    
    #url(r'^sss/', include('ss.sss.urls')),
    #url(r'^login/', views.login, name='firstform'),
    
    #url(r'^(?P<pk>[0-9]+)/$', views.BeerDetail.as_view()),
#    url(r'^secondform/', views.secondform, name='secondform'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
]
if not settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Serializers define the API representation.


# Routers provide an easy way of automatically determining the URL conf.

