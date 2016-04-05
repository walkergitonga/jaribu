from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.inquiry_list, name='inquiry_list'),
]