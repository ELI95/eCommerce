from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django import forms


def validate_short_text(value):
    """
    the length of the content should be longer than 5.
    """
    if len(value) <= 5:
        raise ValidationError(_("Sorry, the length of the content should be longer than 5"), code='invalid')


class LongerTextField(forms.CharField):
    description = "the length of the content should be longer than 5."

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 200
        kwargs['validators'] = [validate_short_text]
        super(LongerTextField, self).__init__(*args, **kwargs)