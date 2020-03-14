from django import forms
from .models import Blog


class CreateBlog(forms.ModelForm):
    class Meta:
        model = Blog
        exclude = []
        fields = ['title', 'author', 'body']