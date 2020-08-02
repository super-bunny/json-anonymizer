import string
from random import randrange, choice, choices


def anonymize(data, empty_string=False):
    data_type = type(data)
    if data_type is list:
        new_data = []
        for item in data:
            new_data.append(anonymize(item, empty_string=empty_string))
        return new_data
    if data_type is dict:
        new_data = {}
        for item in data.items():
            new_data[item[0]] = anonymize(item[1], empty_string=empty_string)
        return new_data
    if data_type is int:
        return anonymize_int(data)
    if data_type is str:
        return anonymize_str(data, empty_string)
    if data_type is bool:
        return anonymize_bool(data)
    return data


def anonymize_int(data: int) -> int:
    length = len(str(data))
    return randrange(10 ** (length - 1), 10 ** length - 1)


def anonymize_str(data: str, empty_string=False) -> str:
    if empty_string:
        return ''
    return ''.join(choices(string.ascii_letters + string.digits, k=len(data)))


def anonymize_bool(data: bool) -> bool:
    return choice([True, False])
