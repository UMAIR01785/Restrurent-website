from django.core.exceptions import ValidationError
import os

def validator_error(value):
    ex=os.path.splitext(value.name)[1]
    print(ex)
    validate_error=['.png','jpg','jpeg']
    if not ex.lower() is validator_error:
        raise ValidationError("This file is not supported please try these :" + str(validate_error))