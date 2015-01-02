from django import forms
from django.forms import DateTimeField, ChoiceField, CharField, URLField
from .models import Project, ProjectFile, Bio
from bootstrap3_datetime.widgets import DateTimePicker


class ProjectForm(forms.ModelForm):
    date_completed = DateTimeField(required=False, label="Date Completed", widget=DateTimePicker(options={"format": "YYYY-MM-DD", "pickTime": False}))
    site_url = URLField(required=False, label=None)

    class Meta:
        model = Project
        fields = (
            'name',
            'description',
            'date_completed',
            'team',
            'site_url', 
        )

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        kwargs['project'] = kwargs.get("instance")

    #TODO: make this stop buggin' out
    def save(self, *args, **kwargs):
        super(ProjectForm, self).save(*args, **kwargs)


#TODO: write bio forms, contact forms, project forms, blag forms & more. 
class BioForm(forms.ModelForm):
    class Meta:
        model = Bio
        fields = (
            'content',
        )
