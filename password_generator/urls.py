from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home, name='home2'),
    path('pwgen', views.pwgen, name='pwgen'),
    path('about', views.about, name='about'),

]
