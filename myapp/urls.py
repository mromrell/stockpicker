from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'yo/', views.yo, name='yo'),  # this is a just a test line
]