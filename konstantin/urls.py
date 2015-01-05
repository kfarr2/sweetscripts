from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from konstantin.blog import views as blog
from konstantin.home import views as home
from konstantin.files import views as files
from konstantin.stuff import views as stuff


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'konstantin.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', home.admin, name='admin'),
    url(r'^login/admin/?$', home.admin_login, name='admin-login'),
    url(r'^$', home.home, name='home'),
    url(r'^files/?$', files.list_, name='files-list'),

    url(r'^about/?$', home.about, name='about'),

    url(r'^stuff/?$', stuff.list, name='stuff'),	

    # Projects
    url(r'^stuff/admin/create/project/?$', stuff.create, name='stuff-create'),
    url(r'^stuff/admin/(?P<project_id>\d+)/?$', stuff.edit, name='stuff-edit'),
    url(r'^stuff/admin/(?P<project_id>\d+)/delete/?$', stuff.delete_project, name='stuff-delete-project'),

    # Contact
    url(r'^contact/?$', stuff.contact, name='contact'),

    # Blog
    url(r'^blog/?$', blog.list_, name='blog'),
    url(r'^blog/create/?$', blog.create, name='blog-create'),
    url(r'^blog/(?P<post_id>\d+)/edit/?$', blog.edit, name='blog-edit'),
)
