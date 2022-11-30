from session_folder.create_session import create_session
from access_create_acc.register_login import register, login
from sqlalchemy import create_engine


def user_account(connection_string, schema):

    engine = create_engine(connection_string)
    session = create_session(engine)

    starting_message = "Choose an option: Register | Login..."

    print(starting_message)

    user_choice = input("I want to...")

    if user_choice.lower() == "register":
        register(session, schema)

    if user_choice.lower() == "login":
        print(login(session, schema))
