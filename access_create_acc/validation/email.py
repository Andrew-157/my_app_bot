import re


def email_validation(value):

    check_match = re.search(
        r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+", value)

    if check_match:
        return True

    return False
