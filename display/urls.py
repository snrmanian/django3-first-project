from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home1'),
    path('show_tables',views.show_tables,name='show_tables'),
    path('add',views.add_student,name='add_student')

]
