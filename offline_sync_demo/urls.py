from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'offline_sync_demo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^poll/$', 'sync.views.poll'),
    url(r'^sync/$', 'sync.views.sync'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'tasks.views.home'),
)
