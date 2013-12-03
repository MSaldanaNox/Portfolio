from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Portfolio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$','MyPortfolio.views.index' ),
    url(r'^menu','MyPortfolio.views.menu' )
    #url(r'^admin/', include(admin.site.urls)),
)
