from __future__ import print_function
import datetime
import sys


from django import forms
from django.forms.fields import Field
from django.forms.models import BaseModelFormSet
from django.forms.formsets import BaseFormSet
from django.forms.util import ErrorDict
from django.template import add_to_builtins
from django.contrib.admin.util import NestedObjects
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth import get_user_model
from django.conf import settings
from django.core.signals import request_started
from django.dispatch import receiver
from django.utils.importlib import import_module
from django.utils.six import add_metaclass

from .forms import Form


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

'''
Old shit. Delete. Possibly.


forms.Form.required_css_class = "required"
forms.ModelForm.required_css_class = "required"
Field.required_css_class = "required"

add_to_builtins('django.contrib.staticfiles.templatetags.staticfiles')
add_to_builtins('konstantin.utils.templatetags.sickform')

# add some helpful methods to the formset
class FormSetMixin(object):
	def iter_with_empty_form_first(self):
		"""
		Iterates over the forms in this formset, but the first form yielded
		is the empty one. This simplifies the logic in templates, since the
		empty_form is no longer a special case
		"""
		yield self.empty_form
		for form in iter(self):
			yield form
	
	def clean(self):
		"""
		When cleaning, if the form is being deleted, any errors on it should be
		ignored
		"""
		for form in self.forms:
			# this form is being deleted, so overwrite the errors
			if form.cleaned_data.get("DELETE"):
				form._errors = ErrorDict()

# add the FormSetMixin to the base FormSet classes
class BaseFormSet(FormSetMixin, BaseFormSet): pass
class BaseModelFormSet(FormSetMixin, BaseModelFormSet): pass


def dictfetchall(cursor):
	"""Returns all rows from a cursor as a dict"""
	desc = cursor.description
	return [
		dict(zip([col[0] for col in desc], row))
		for row in cursor.fetchall()
	]

'''
