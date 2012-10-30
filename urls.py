from django.conf.urls import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wiki.views.home', name='home'),
    # url(r'^wiki/', include('wiki.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
   # url(r'^admin/', include(admin.site.urls)),
  	  url(r'^accounts/' include(' registration.backends.default.url')),
  	  ulr(r'^admin/', include(admin.site.urls)),
  	  url(r'^pastebin/', include('pastebin.urls')),
  	  url(r'^blog/', include('blog.urls')),
)
