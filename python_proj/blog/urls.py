'''
Created on 2020. 4. 30.

@author: ahntonio
'''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]