

def password_validate(value):

    if len(value) > 20:

        return "Your password is too long, try another one, please"

    elif len(value) < 7:

        return "You password is too short, try another one, please"

    return False
