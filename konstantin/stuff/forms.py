from django import forms
from django.forms import DateTimeField, ChoiceField, CharField
from .models import Project, ProjectFile
from bootstrap3_datetime.widgets import DateTimePicker

class ProjectForm(forms.ModelForm):
	date_completed = DateTimeField(required=False, label="Date Completed", widget=DateTimePicker(options={"format": "YYYY-MM-DD", "pickTime": False}))

	class Meta:
		model = Project
		fields = (
			'name',
			'description',
			'date_completed',
			'team',
			'screenshot',
			'site_url',	
		)

	def __init__(self, *args, **kwargs):
		super(ProjectForm, self).__init__(*args, **kwargs)
	
	def save(self, *args, **kwargs):
		to_return = super(ProjectForm, self).save(*args, **kwargs)
		return to_return
