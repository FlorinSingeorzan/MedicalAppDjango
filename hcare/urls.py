from django.conf.urls import url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    url(r'index.html$', views.index, name='index'),
    # url(r'register.html$', views.register, name='register'),
    url(r'^(?P<doctor_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^doc/$', views.home, name='user'),
    url(r'^message_sent/$', views.send, name='send'),
    url(r'^respond/$', views.respond, name='respond'),
    url(r'^messages/$', views.view_messages, name='messages'),
    url(r'^feed/$', views.feed, name='feed'),
]

urlpatterns += staticfiles_urlpatterns()
