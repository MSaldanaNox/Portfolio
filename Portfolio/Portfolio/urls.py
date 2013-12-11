from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Portfolio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$','MyPortfolio.views.home' ),
    url(r'^Home','MyPortfolio.views.home' ),
    url(r'^About','MyPortfolio.views.about' ),
    url(r'^Projects','MyPortfolio.views.projects' ),
    url(r'^Illustrations','MyPortfolio.views.illustrations' ),
    url(r'^Templates','MyPortfolio.views.templates' ),
    #url(r'^admin/', include(admin.site.urls)),
)
