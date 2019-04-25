# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, String
from sqlalchemy.schema import FetchedValue
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class TesUsr(Base):
    __tablename__ = 'tes_usr'

    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)


class User(Base):
    __tablename__ = 'user'

    uid = Column(BigInteger, primary_key=True)
    nickname = Column(String(100), nullable=False, server_default=FetchedValue())
    mobile = Column(String(20), nullable=False, server_default=FetchedValue())
    email = Column(String(100), nullable=False, server_default=FetchedValue())
    sex = Column(Integer, nullable=False, server_default=FetchedValue())
    avatar = Column(String(64), nullable=False, server_default=FetchedValue())
    login_name = Column(String(20), nullable=False, unique=True, server_default=FetchedValue())
    login_pwd = Column(String(32), nullable=False, server_default=FetchedValue())
    login_salt = Column(String(32), nullable=False, server_default=FetchedValue())
    status = Column(Integer, nullable=False, server_default=FetchedValue())
    updated_time = Column(DateTime, nullable=False, server_default=FetchedValue())
    created_time = Column(DateTime, nullable=False, server_default=FetchedValue())
