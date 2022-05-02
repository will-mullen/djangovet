from django.urls import path
# from . import views
from django.conf.urls import url 
from vetoffice import views
from vetoffice.models import FB_N_01, Red_Line_Tracking

urlpatterns = [
    path('', views.home),
    url(r'^customers$', views.customersApi),
    url(r'^customers/([0-9]+)$', views.customersApi),
    url(r'^FB_N_01$', views.FB_N_01_Api, name='FB_N_01'),
    url(r'^Red_Line_Tracking$', views.Red_Line_Tracking_Api, name='Red_Line_Tracking'),
    path('FB_N_01/<pk>', views.FB_N_01_Api, name='FB_N_01_detailed'),
    path('Red_Line_Tracking/<pk>', views.Red_Line_Tracking_Api, name='Red_Line_Tracking_detailed')
]