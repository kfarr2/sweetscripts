from django import forms
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    is_public = forms.CheckboxInput()
    allow_comments = forms.CheckboxInput()

    class Meta:
        model = BlogPost
        fields = (
            'title',
            'content',
            'is_public',
            'allow_comments',
        )

