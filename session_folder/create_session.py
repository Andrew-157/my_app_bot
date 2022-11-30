from sqlalchemy.orm import sessionmaker


def create_session(engine):

    Session = sessionmaker(bind=engine)
    session = Session()

    return session
