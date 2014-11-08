from django import forms
from django.template import Context
from django.template.loader import get_template
from django import template
from django.conf import settings

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

def add_input_classes(field):
	if takes_input(field):
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
def takes_input(field):
	input = not isinstance(field.field.widget, forms.CheckboxInput)
	input = input and not isinstance(field.field.widget, forms.CheckboxSelectMultiple)
	input = input and not isinstance(field.field.widget, forms.RadioSelect)
	input = input and not isinstance(field.field.widget, forms.FileInput)
	return takes_input == True

