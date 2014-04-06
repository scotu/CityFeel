from django.conf.urls import patterns, include, url
from django.contrib import admin
from core import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'battlehack2014.views.home', name='home'),
    # url(r'^battlehack2014/', include('battlehack2014.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^$', views.index, name="index"),
    url(r'^map/$', views.map, name="map"),
    url(r'^data/$', views.data, name="data"),
    url(r'^ohhhhh/$', views.ohhhhh),
    url(r'^admin/', include(admin.site.urls)),
)
