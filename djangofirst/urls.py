from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^readj', views.readj, name='readj'),
    url('prova', views.prova, name='prova'),
    url(r'^listuser', views.listuser, name='listuser'),
    url(r'^createJsonList', views.createJsonList, name='createJsonList'),




]