from django import forms
from .models import Blog, Comment

class CreateBlog(forms.ModelForm):
    class Meta:
        model = Blog
        exclude = []
        fields = ['title', 'author', 'body']

class BlogCommentForm(forms.ModelForm):
    class Meta:
        model = Comment

        fields = ['comment_textfield']
        widgets = {
            'comment_textfield': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 40})
        }