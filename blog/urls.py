from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.BlogIndex.as_view(), name='index'),
    url(r"^(?P<pk>[0-9]+)/tag/$", views.blogTag, name='tag'),
    url(r"^blog/(?P<pk>[0-9]+)$", views.BlogPost.as_view(), name='blogpost')

]
