from random import randrange, choice


def anonymize(data):
    data_type = type(data)
    if data_type is list:
        new_data = []
        for item in data:
            new_data.append(anonymize(item))
        return new_data
    if data_type is dict:
        new_data = {}
        for item in data.items():
            new_data[item[0]] = anonymize(item[1])
        return new_data
    if data_type is int:
        return anonymize_int(data)
    if data_type is str:
        return anonymize_str(data)
    if data_type is bool:
        return anonymize_bool(data)
    return data


def anonymize_int(data: int) -> int:
    length = len(str(data))
    return randrange(10 ** (length - 1), 10 ** length - 1)


def anonymize_str(data: str) -> str:
    return ""


def anonymize_bool(data: bool) -> bool:
    return choice([True, False])
