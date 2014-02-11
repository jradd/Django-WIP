from django.conf.urls import patterns, include
from django.contrib import admin
from django.views.generic import TemplateView


admin.autodiscover()

urlpatterns = patterns('', (r'^weblog/', include('mysecuri.blog.urls')),
    (r'^$', TemplateView.as_view(template_name="home.html")),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
)
