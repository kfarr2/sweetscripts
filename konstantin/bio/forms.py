from django import forms

#TODO: write bio forms, contact forms, project forms, blag forms & more. 
class BioForm(forms.ModelForm):
    is_public = BooleanField(required=False)


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


