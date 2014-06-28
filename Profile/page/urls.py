from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
        url(r'^user/(?P<user_id>\d+)/$', 'page.views.user_profile'),
)

