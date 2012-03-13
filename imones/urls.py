from django.conf.urls.defaults import patterns, include, url
from imones.views import *

urlpatterns = patterns('',
    (r'^$', companies),     
    (r'^users/$', users),
    (r'^details/(?P<id>\d+)$', company_detail),
) 


