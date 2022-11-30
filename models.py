from sqlalchemy import Column, Integer, Date, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base


class Account(Base):

    __tablename__ = 'Accounts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
