from django.urls import path
from . import views

urlspattens=[
    path('',views.home,name='home')
]