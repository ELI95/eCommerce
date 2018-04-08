from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django import forms
from django.db import models


def validate_short_text(value):
    """
    the length of the content should be longer than 5.
    """
    if len(value) <= 5:
        raise ValidationError(_("Sorry, the length of the content should be longer than 5"), code='invalid')


class LongerTextFormField(forms.CharField):
    description = "the length of the content should be longer than 5."

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 200
        kwargs['validators'] = [validate_short_text]
        super(LongerTextFormField, self).__init__(*args, **kwargs)


class LongerTextModelField(models.CharField):
    description = "the length of the content should be longer than 5."

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 200
        kwargs['validators'] = [validate_short_text]
        super(LongerTextModelField, self).__init__(*args, **kwargs)
