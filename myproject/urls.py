from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^cms/$', 'cms.views.mostrar'),
    url(r'^cms/(\d+)', 'cms.views.pagina'),
    url(r'^admin/', include(admin.site.urls)),
)
