from session_folder import create_session
from sqlalchemy import create_engine


def main(connection_string):

    engine = create_engine(connection_string)
    session = create_session(engine)
