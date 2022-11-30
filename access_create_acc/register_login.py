from access_create_acc.validation.email import email_validation
from access_create_acc.validation.name import name_validation
from access_create_acc.validation.password import password_validate


def login(session, schema):
    user_status = ""

    while True:
        user_name = input("Enter your name: ")

        if session.query(schema).filter_by(name=user_name).first():
            break
        else:
            print(f"Account with name {user_name} doesn't exist")
            continue

    while True:
        user_email = input("Enter your email: ")

        if session.query(schema).filter_by(email=user_email).first():
            break
        else:
            print(f"{user_name} user doesn't have this email {user_email}")
            continue

    counter = 0

    while True:
        user_password = input("Enter your password: ")

        if session.query(schema).filter_by(password=user_password).first() and session.query(schema).filter_by(name=user_name).first():
            user_status = "Successfully entered the account"
            break

        else:
            counter += 1
            print("Wrong password, try again...")
            if counter == 3:
                user_status = "Failed to enter the account, wrong password"
                break

    return user_status


def register(session, schema):

    while True:
        user_name = input("Enter name for your account: ")

        if session.query(schema).filter_by(name=user_name).first():
            print(
                f"Account with {user_name} already exists, try another name, please")
            continue

        if not name_validation(user_name):
            break
        else:
            print(name_validation(user_name))
            continue

    while True:
        user_email = input("Enter email for you account: ")

        if session.query(schema).filter_by(email=user_email).first():
            print(
                f"Account with this email: {user_email} already exists, try another one, please")
            continue

        if email_validation(user_email):
            break

        else:
            print(f"{user_email} is of the wrong format, try another, please")
            continue

    while True:
        user_password = input("Enter password for your account: ")

        if password_validate(user_password):
            print(password_validate(user_password))
            continue

        else:
            break

    new_account = schema(name=user_name, email=user_email,
                         password=user_password)
    session.add(new_account)
    session.commit()

    return "Account was successfully created!"
