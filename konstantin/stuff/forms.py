from bootstrap3_datetime.widgets import DateTimePicker
from django import forms
from django.forms import DateTimeField, ChoiceField, CharField, URLField, MultipleChoiceField, BooleanField
from .models import Project, ProjectFile, Bio, Blog
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
        kwargs['project'] = kwargs.get('instance')
        self.fields['type'].choices = ProjectType
        self.fields['current_state'].choices = ProjectState
        self.fields['role'].choices = ProjectRole

    def save(self, *args, **kwargs):
        super(ProjectForm, self).save(*args, **kwargs)


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


class BlogForm(forms.ModelForm):
    is_public = BooleanField(required=False)

    class Meta:
        model = Blog
        fields = (
            'title',
            'post',
            'is_public',
        )

    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)
    
    def save(self, *args, **kwargs):
        super(BlogForm, self).save(*args, **kwargs)
