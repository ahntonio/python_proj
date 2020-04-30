'''
Created on 2020. 4. 26.

@author: ahntonio
'''
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]