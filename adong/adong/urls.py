from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib.auth.views import login,logout

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'adong.views.home', name='home'),
    # url(r'^adong/', include('adong.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    (r'^$', 'homepage.views.index'),
    (r'^home/help/', 'homepage.views.help'),
    (r'^accounts/login', login, {'template_name':'homepage/login.html'}),
    (r'^accounts/logout', logout, {'template_name':'homepage/logout.html'}),
    (r'^accounts/profile', 'homepage.views.profile'),
    (r'^accounts/changepwd', 'homepage.views.changepwd'),
)

urlpatterns += patterns('blog.views',
    (r'^blog/', 'index'),
)

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
