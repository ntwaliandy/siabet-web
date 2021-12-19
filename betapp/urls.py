from os import name
from django.urls import path
from django.conf.urls import url
from . import views
app_name = 'betapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('board/', views.board, name="board"),
    path('suggest/', views.suggest, name='suggest'),
    path('requests/', views.requests, name='requests'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
]