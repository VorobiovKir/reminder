from django.conf.urls import include, url

urlpatterns = [

    # url(r'^$', 'authorization.views.home', name='home'),
    url(r'^login/$', 'authorization.views.login', name='login'),
    url(r'^registration/$', 'authorization.views.registration', name='regist'),
    url(r'^logout/$', 'authorization.views.logout'),
]