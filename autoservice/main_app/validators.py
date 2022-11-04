import phonenumbers
from django.core.exceptions import ValidationError


def validate_phone(number: str) -> None:
    """
    Валидация номера телефона.

    :param number: Стандартный номер телефона.
    :return: True, если номер телефона валиден, иначе False.
    """

    # Возможно, отсутствует символ плюса.
    if not number.startswith('+'):
        number = '+' + number

    error = ValidationError('Неверный номер телефона')

    # Парсим номер телефона в объект.
    try:
        phone_obj = phonenumbers.parse(number)
    except phonenumbers.NumberParseException:
        raise error

    # Проверяем на валидность кода страны, кода оператор и кол-во
    # цифр в зависимости от страны.
    if not phonenumbers.is_valid_number(phone_obj):
        raise error