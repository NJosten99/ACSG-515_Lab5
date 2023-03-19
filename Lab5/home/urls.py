from django.urls import path 
from . import views

#This makes default the html page rendered by index in the views file
urlpatterns = [
    path('', views.index, name='index')
]