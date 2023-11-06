from . import calculation as calc
from . import compatible as compat


@compat.check_special_characters
def validate(cpf_number):
    """This function validates a CPF number.

    This function uses calculation package to calculate both digits
    and then validates the number.

    :param cpf_number: a CPF number to be validated.  Only numbers.
    :type cpf_number: string
    :return: Bool -- True for a valid number, False otherwise.

    """

    _cpf = compat.clear_punctuation(cpf_number)

    if len(_cpf) != 11 or len(set(_cpf)) == 1:
        return False

    first_part = _cpf[:9]
    second_part = _cpf[:10]
    first_digit = _cpf[9]
    second_digit = _cpf[10]

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