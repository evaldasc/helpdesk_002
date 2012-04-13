from django.conf.urls.defaults import patterns, include, url
from core.views import *

urlpatterns = patterns('',
    (r'^$', companies),  
    (r'^companies/$', companies),  
    (r'^companies/list/$', companies),    
    (r'^companies/details/(?P<id>\d+)/$', company_detail),
    (r'^companies/details/(?P<id>\d+)/users/list/$', company_users),
    (r'^users/details/(?P<id>\d+)/$', user_detail),
) 
