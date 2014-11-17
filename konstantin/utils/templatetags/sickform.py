from django import forms
from django.template import Context
from django.template.loader import get_template
from django import template
from django.conf import settings
from django.template.defaulttags import url
from django.core.urlresolvers import reverse
from django.template import Node, Variable, VariableDoesNotExist
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

TOTAL_PAGE_COLUMNS = getattr(settings, 'TOTAL_PAGE_COLUMNS', 12)

register = template.Library()

@register.filter
def sickform(element):
	if not element:
		return ""

	markup_classes = {'label': '', 'value': '', 'single_value': ''}
	return render(element, markup_classes)

@register.filter
def sickform_inline(element):
	if not element:
		return ""

	markup_classes = {'label': 'sr-only', 'value': '', 'single_value': ''}
	return render(element, markup_classes)

@register.filter
def sickform_horizontal(element, label_cols={}):
	if not element:
		return ""

	if not label_cols:
		label_cols = "col-sm-2 col-lg-2"

	for cl in label_cols.split(' '):
		splitted_class = cl.split('-')

		try:
			value_nb_cols = int(splitted_class[-1])
		except ValueError:
			value_nb_cols = TOTAL_PAGE_COLUMNS

		if value_nb_cols >= TOTAL_PAGE_COLUMNS:
			splitted_class = TOTAL_PAGE_COLUMNS
		else:
			offset_class = cl.split('-')
			offset_class[-1] = 'offset' + str(value_nb_cols)
			splitted_class[-1] = str(TOTAL_PAGE_COLUMNS - value_nb_cols)
			markup_classes['single_value'] += ' ' + '-'.join(offset_class)
			markup_classes['single_value'] += ' ' + '-'.join(markup_class)

		

def add_input_classes(field):
	if not is_checkbox(field) and not is_multiple_checkbox(field) and not is_radio(field) and not is_file(field):		
		field_classes = field.field.widget.attrs.get('class', '')
		field_classes += ' form_control'
		field.field.widget.attrs['class'] = field_classes

def render(element, markup_classes):
	element_type = element.__class__.__name__.lower()

	if element_type == 'boundfield':
		add_input_classes(element)
		template = get_template('sickform/field.html')
		context = Context({'formset': element, 'classes': markup_classes})
	else:
		has_management = getattr(element, 'management_form', None)
		if has_management:
			for form in element.forms:
				for field in form.visible_fields():
					add_input_classes(field)
			
			template = get_template("sickform/formset.html")
			context = Context({'form': element, 'classes': markup_classes})
		else:
			for field in element.visible_fields():
				add_input_classes(field)
			
			template = get_template("sickform/form.html")
			context = Context({'form': element, 'classes': markup_classes})

@register.filter
def is_checkbox(field):
	return isinstance(field.field.widget, forms.CheckboxInput)

@register.filter
def is_multiple_checkbox(field):
	return isinstance(field.field.widget, forms.CheckboxSelectMultiple)

@register.filter
def is_radio(field):
	return isinstance(field.field.widget, forms.RadioSelect)

@register.filter
def is_file(field):
	return isinstance(field.field.widget, forms.FileInput)
