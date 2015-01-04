from bootstrap3_datetime.widgets import DateTimePicker
from django import forms
from django.forms import DateTimeField, ChoiceField, CharField, URLField, MultipleChoiceField
from .models import Project, ProjectFile, Bio
from .enums import ProjectState, ProjectType, ProjectRole


class ProjectForm(forms.ModelForm):
    date_completed = DateTimeField(required=False, label="Date Completed", widget=DateTimePicker(options={"format": "YYYY-MM-DD", "pickTime": False}))
    site_url = URLField(required=False, label=None)
    role = MultipleChoiceField(required=True, label="Role")
    type = ChoiceField(required=True, label="Project Type")
    current_state = ChoiceField(required=True, label="Project State")

    class Meta:
        model = Project
        fields = (
            'name',
            'description',
            'date_completed',
            'team',
            'site_url', 
            'role',
            'type',
            'current_state',
        )

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        kwargs['project'] = kwargs.get("instance")
        self.fields['type'].choices = ProjectType
        self.fields['current_state'].choices = ProjectState
        self.fields['role'].choices = ProjectRole

    def save(self, *args, **kwargs):
        super(ProjectForm, self).save(*args, **kwargs)


#TODO: write bio forms, contact forms, project forms, blag forms & more. 
class BioForm(forms.ModelForm):
    class Meta:
        model = Bio
        fields = (
            'content',
        )
