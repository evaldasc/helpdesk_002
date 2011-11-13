from django.conf.urls.defaults import patterns, include, url
from imones.views import *

urlpatterns = patterns('',
    (r'^$', imones),     
    (r'^users/$', users),
) 


