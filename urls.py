from django.conf.urls.defaults import patterns, include, url
from helpdesk_002.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    (r'^login/$', 'django.contrib.auth.views.login'),

    # Login / logout.
    (r'^$', 'django.contrib.auth.views.login'),
    (r'^logout/$', logout_page),

    # Web portal.
    (r'^imones/', include('helpdesk_002.imones.urls')),

    # Serve static content.
    #(r'^static/(?P<path>.*)$', 'django.views.static.serve',
    #    {'document_root': 'static'}),
)
