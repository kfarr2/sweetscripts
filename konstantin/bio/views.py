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
    edit = Bio.objects.first()

    if request.method == "POST":
        form = BioForm(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('about'))
    else:
        form = BioForm(instance=edit)


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

def contact_edit(request):
    """
    Edit contact info
    """
    contact = Contact.objects.first()

    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('contact'))
    else:
        form = ContactForm(instance=contact)

    return render(request, 'bio/contact_edit.html', {
        'form': form,    
    })
