from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.inquiry_list, name='inquiry_list'),
    url(r'^inquiry/(?P<pk>\d+)/$', views.inquiry_detail, name='inquiry_detail'),
    url(r'^inquiry/new/$', views.inquiry_new, name='inquiry_new'),
    url(r'^inquiry/(?P<pk>\d+)/edit/$', views.inquiry_edit, name='inquiry_edit'),
]