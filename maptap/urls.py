from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from maptap import views

urlpatterns = patterns('',
    url(r'^pull/$', views.pull, name = 'pull'),
    url(r'^pull_search/$', views.pull_search, name = 'pull_search'),
    url(r'^push/$', views.push, name = 'push'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'writing/login.html'}, name = 'login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page' : '/writing/'}, name = 'logout'),
    url(r'^$', views.IndexView, name='index'),
    url(r'^add_user/$', views.add_user, name = 'add_user'),
    url(r'^addpaper/$', views.add_paper, name='add_paper'),
    url(r'^(?P<t>[\w|\W]+)/$', views.paper, name = 'paper'),
)
