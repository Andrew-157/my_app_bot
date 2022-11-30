
def name_validation(value):

    if len(value) > 50:

        return f"{value} is too long, try another one"

    if len(value) < 5:

        return f"{value} is too short, try another one"

    return False
