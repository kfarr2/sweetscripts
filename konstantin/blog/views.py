from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from .models import BlogPost
from .forms import BlogPostForm
# Create your views here.


def list_(request):
    """
    list all blog posts
    """
    posts = BlogPost.objects.all()

    return render(request, 'blog/list.html',{
        'posts': posts,
    })

@login_required
def create(request):
    """
    Create a new blog post
    """
    return edit_(request, post_id=None)

@login_required
def edit(request, post_id):
    """
    Edit an existing post.
    """
    return edit_(request, post_id)

@login_required
def edit_(request, post_id):
    """
    Do all the actual work.
    """
    if post_id is not None:
        post = get_object_or_404(BlogPost, pk=post_id)
    else:
        post = None


    if request.POST:
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blog'))

    else:
        form = BlogPostForm(instance=post)

    return render(request, 'blog/edit.html', {
        'form': form,
    })

