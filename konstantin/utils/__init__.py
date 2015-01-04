from __future__ import print_function
import datetime
import sys
import time

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


class IterableChoiceEnum(type): #NOTE: Original written by PSU-OIT-ARC

    def __init__(cls, name, bases, attrs):
        cls._choices_dict = dict(cls)

    def __iter__(cls):
        """Simply return the iterator of the _choices tuple"""
        return iter(cls._choices)

    def __getitem__(cls, choice):
        """Return choice description via item access.

        Example::

            >>> class MyEnum(ChoiceEnum):
            ...
            ...     A = 1
            ...     B = 2
            ...
            ...     _choices = (
            ...         (A, 'Alpha'),
            ...         (B, 'Beta'),
            ...     )
            ...
            >>> MyEnum[MyEnum.A]
            'Alpha'

        """
        return cls._choices_dict[choice]

    def get(cls, choice, default=None):
        try:
            return cls[choice]
        except KeyError:
            return default


@add_metaclass(IterableChoiceEnum)
class ChoiceEnum(object):
    """
    This creates an iterable *class* (as opposed to an iterable *instance* of a
    class). Subclasses must define a class variable called `_choices` which is a
    list of 2-tuples. Subclasses can be passed directly to a field as the
    `choice` kwarg.

    For example:

    class FooType(ChoiceEnum):
        A = 1
        B = 2

        _choices = (
            (A, "Alpha"),
            (B, "Beta"),
        )


    class SomeModel(models.Model):
        foo = models.ChoiceField(choices=FooType)
    """
    _choices = ()
    # http://stackoverflow.com/questions/5434401/python-is-it-possible-to-make-a-class-iterable-using-the-standard-syntax

