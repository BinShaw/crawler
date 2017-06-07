from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index', views.test, name='test'),
    # url(r'^article/(?P<article_id>[0-9]+)/$', views.detail, name='detail'),
]
