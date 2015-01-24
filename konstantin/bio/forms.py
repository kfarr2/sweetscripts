from django import forms
from .models import Bio, Contact


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
        kwargs['bio'] = kwargs.get('instance')

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

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        kwargs['contact'] = kwargs.get('instance')
