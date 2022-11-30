from session_folder import create_session
from register_login import register, login
from sqlalchemy import create_engine
from models import Account


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
