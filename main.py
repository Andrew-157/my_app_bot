from session_folder import create_session
from sqlalchemy import create_engine


def main(connection_string):

    engine = create_engine(connection_string)
    session = create_session(engine)

    print("Welcome!")

    starting_message = "Choose an option: Register | Login..."

    user_choice = input("I want to...")

    if user_choice.lower() == "register":
        pass

    if user_choice.lower() == "login":
        pass
