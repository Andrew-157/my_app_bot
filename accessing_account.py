from session_folder import create_session
from sqlalchemy import create_engine
from models import Account
from sqlalchemy.sql import sql


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
            user_status = "Successfully entered account"
            break

        else:
            counter += 1
            print("Wrong password, try again...")
            if counter == 3:
                user_status = "Failed to enter the account, wrong password"
                break

    return user_status


def register(session, schema: Account):

    while True:
        user_name = input("Enter name for your account: ")

        if session.query(schema).filter_by(name=user_name).first():
            print(
                f"Account with {user_name} already exists, try another name, please")
            continue

        else:
            break

    while True:
        user_email = input("Enter email for you account: ")

        if session.query(schema).filter_by(email=user_email).first():
            print(
                f"Account with this email: {user_email} already exists, try another one, please")
            continue

        else:
            break

    user_password = input("Enter password for your account: ")

    new_account = schema(name=user_name, email=user_email,
                         user_password=user_password)

    return "Account was successfully created!"


def accessing_account(connection_string, schema):

    engine = create_engine(connection_string)
    session = create_session(engine)

    starting_message = "Choose an option: Register | Login..."

    print(starting_message)

    user_choice = input("I want to...")

    if user_choice.lower() == "register":
        register(session, schema)

    if user_choice.lower() == "login":
        print(login(session, schema))
