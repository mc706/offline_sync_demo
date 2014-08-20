from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = patterns('',
    url(r'^login/$', 'accounts.views.login_user', name='login'),
    url(r'^register/$', 'accounts.views.register', name='register'),
    url(r'^sync/$', 'sync.views.sync'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index.html$', 'tasks.views.home', name='home'),
    url(r'^$', 'tasks.views.home', name='home'),
)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)