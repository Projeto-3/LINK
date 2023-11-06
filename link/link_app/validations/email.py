from django.core.exceptions import ValidationError
from django.core.validators import validate_email

#puxar input do usuario do forms.py
value = "foo.bar@baz.qux"

try:
    validate_email(value)
except ValidationError as e:
    print("Email inválido", e)
else:
    print("sucesso!")