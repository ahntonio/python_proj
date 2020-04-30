'''
Created on 2020. 4. 26.

@author: ahntonio
'''
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
