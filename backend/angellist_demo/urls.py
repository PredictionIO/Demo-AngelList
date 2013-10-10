from django.conf.urls.defaults import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from startups import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'angellist_demo.views.home', name='home'),
    # url(r'^angellist_demo/', include('angellist_demo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^startups$', views.StartupList.as_view()),
    url(r'^startups/(?P<pk>[0-9]+)$', views.StartupDetail.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)
