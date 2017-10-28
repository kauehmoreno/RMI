# -- coding: utf-8 --
from django.conf.urls import url
from remote import views

urlpatterns = [
    url(r'^$', views.rmi_post, name='post'),
]
