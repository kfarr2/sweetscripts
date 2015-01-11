from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Bio, Contact
from .forms import BioForm, ContactForm

def about(request):
    """
    about
    """
    bio = Bio.objects.first()
    return render(request, 'bio/about.html', {
        'bio' : bio,
    })

def about_edit(request):
    """
    edit bio
    """
    if request.method == "POST":
        form = BioForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('about'))
    else:
        form = BioForm()


    return render(request, 'bio/about_edit.html', {
        'form': form,        
    })



def contact(request):
    """
    Contact
    """
    contact = Contact.objects.first() 
    return render(request, 'bio/contact.html', {
        'contact': contact,
    })
