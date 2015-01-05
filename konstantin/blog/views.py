from django.shortcuts import render
from django.core.urlresolvers import reverse
from konstantin.blog.models import BlogPost
# Create your views here.

def list_(request):
    """
    list all blog posts
    """

    return render(request, 'blog/list.html',{
            
    })
