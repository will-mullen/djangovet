from django.urls import path
# from . import views
from django.conf.urls import url 
from vetoffice import views

urlpatterns = [
    path('', views.home),
    url(r'^customers$', views.customersApi),
    url(r'^customers/([0-9]+)$', views.customersApi)
]