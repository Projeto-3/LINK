from . import calculation as calc
from . import compatible as compat


@compat.check_special_characters
def validate(cnpj_number):
    """This function validates a CNPJ number.

    This function uses calculation package to calculate both digits
    and then validates the number.

    :param cnpj_number: a CNPJ number to be validated.  Only numbers.
    :type cnpj_number: string
    :return: Bool -- True for a valid number, False otherwise.

    """

    _cnpj = compat.clear_punctuation(cnpj_number)

    if len(_cnpj) != 14 or len(set(_cnpj)) == 1:
        return False

    first_part = _cnpj[:12]
    second_part = _cnpj[:13]
    first_digit = _cnpj[12]
    second_digit = _cnpj[13]

    if first_digit == calc.calculate_first_digit(
        first_part
    ) and second_digit == calc.calculate_second_digit(second_part):
        return True
    
def check_special_characters(func):
    def wrapper(document):
        not_digit = [i for i in clear_punctuation(document) if not i.isdigit()]
        return False if not_digit else func(document)

    return wrapper


def clear_punctuation(document):
    """Remove from document all pontuation signals."""
    return document.translate(str.maketrans({".": None, "-": None, "/": None}))

    return False