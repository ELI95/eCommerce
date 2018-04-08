from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.db import models


def validate_rating(value):
    """
    validate the value of rating
    """
    if value < 0 or value > 10:
        raise ValidationError(_("Sorry, the rating should be between 0 and 10"), code='invalid')


class RatingField(models.DecimalField):
    description = "the rating should be between 0 and 10"

    def __init__(self, *args, **kwargs):
        kwargs['max_digits'] = 3
        kwargs['decimal_places'] = 1
        kwargs['validators'] = [validate_rating]
        kwargs['blank'] = True
        kwargs['null'] = True
        super(RatingField, self).__init__(*args, **kwargs)
