
from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [

   path('', views.taskList, name="task"),
   path('reset/', views.reset, name="task1"),
   path("delete/",views.try_first_time,name='fnf'),
]
