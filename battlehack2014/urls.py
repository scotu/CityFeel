from django.conf.urls import patterns, include, url
from django.contrib import admin
from core.views import ohhhhh

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'battlehack2014.views.home', name='home'),
    # url(r'^battlehack2014/', include('battlehack2014.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^ohhhhh/$', ohhhhh),
    url(r'^admin/', include(admin.site.urls)),
)
