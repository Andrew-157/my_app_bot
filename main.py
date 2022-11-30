from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


def create_session(engine):

    Session = sessionmaker(bind=engine)
    session = Session()

    return session


def main(connection_string):

    engine = create_engine(connection_string)
    session = create_session(engine)
