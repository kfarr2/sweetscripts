from django import forms
from .models import Bio, Contact


#TODO: write bio forms, contact forms, project forms, blag forms & more. 
class BioForm(forms.ModelForm):
    is_public = forms.BooleanField(required=False)


    class Meta:
        model = Bio
        fields = (
            'content',
            'is_public',
        )

    def __init__(self, *args, **kwargs):
        super(BioForm, self).__init__(*args, **kwargs)
    
    def save(self, *args, **kwargs):
        super(BioForm, self).save(*args, **kwargs)

class ContactForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    birthday = forms.DateField(required=True)

    class Meta:
        model = Contact
        fields = (
            'first_name',
            'middle_name',
            'last_name',
            'email',

            'birthday',
        )
