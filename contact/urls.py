from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.inquiry_list, name='inquiry_list'),
    url(r'^inquiry/(?P<pk>\d+)/$', views.inquiry_detail, name='inquiry_detail'),
]