'''
Created on 2020. 4. 30.

@author: ahntonio
'''
from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)