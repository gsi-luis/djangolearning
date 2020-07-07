from django.core.exceptions import ValidationError


def validate_number(value):
    if value <= 0 or value > 10:
        raise ValidationError(
            '%(value)  is not greater than 0 and less than 10',
            params={'value': value},
        )
