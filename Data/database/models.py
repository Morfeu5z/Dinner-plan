# coding: utf-8
from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String, Text, FetchedValue
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from . import IConnector
from datetime import date

Connector = IConnector()
Base = Connector.getBase()
# Base = declarative_base()
# Base.query = session.query_property()

"""
class Day(Base):
    __tablename__ = 'day'
    id = Column(Integer, primary_key=True)
    id_dinnerset = Column(ForeignKey('dinnercomposit.id'), index=True)
    day = Column(Date, nullable=False)
    dinnerset = relationship('Dinnercomposit', primaryjoin='Day.id_dinnercomposit == Dinnercomposit.id', backref='days')

    def __init__(self, date : date, id_dinnerset: int):
        self.day = date
        self.id_dinnerset = id_dinnerset
"""

class Dinner(Base):
    __tablename__ = 'dinner'
    id = Column(Integer, primary_key=True)
    dinner = Column(String(50, 'utf8_unicode_ci'), unique=True)
    more = Column(Text(collation='utf8_unicode_ci'))

    def __init__(self, dinner: str, more: str):
        self.dinner = dinner
        self.more = more


class Dinnerset(Base):
    __tablename__ = 'dinnerset'
    id = Column(Integer, primary_key=True)
    id_dinnertype = Column(ForeignKey('dinnertype.id'), index=True)

    dinnertype = relationship('Dinnertype', primaryjoin='Dinnerset.id_dinnertype == Dinnertype.id', backref='dinnersets')
    dinnercomposit = relationship("Dinnercomposit", primaryjoin='Dinnercomposit.id_dinnerset == Dinnerset.id', back_populates="dinnerset")
    userlist = relationship("Userlist", primaryjoin='Userlist.id_dinnerset == Dinnerset.id', back_populates="dinnerset")

    def __init__(self, id_dinnertype: int):
        self.id_dinnertype = id_dinnertype


class Dinnercomposit(Base):
    __tablename__ = 'dinnercomposit'
    id = Column(Integer, primary_key=True)
    id_dinner = Column(ForeignKey('dinner.id'), index=True)
    id_dinnerset = Column(ForeignKey('dinnerset.id'), index=True)
    dinner = relationship('Dinner', primaryjoin='Dinnercomposit.id_dinner == Dinner.id', backref='dinnercomposits')
    dinnerset = relationship('Dinnerset', primaryjoin='Dinnercomposit.id_dinnerset == Dinnerset.id', backref='dinnercomposits')

    def __init__(self, id_dinner, id_dinnerset):
        self.id_dinner = id_dinner
        self.id_dinnerset = id_dinnerset


"""
class Dinnertime(Base):
    __tablename__ = 'dinnertime'
    id = Column(Integer, primary_key=True)
    id_dinnertype = Column(ForeignKey('dinnertype.id'), index=True)
    dinnertype = relationship('Dinnertype', primaryjoin='Dinnertime.id_dinnertype == Dinnertype.id', backref='dinnertimes')

    def __init__(self, id_dinnertype: str):
        self.id_dinnertype = id_dinnertype
"""

class Dinnertype(Base):
    __tablename__ = 'dinnertype'
    id = Column(Integer, primary_key=True)
    dinnertype = Column(String(30, 'utf8_unicode_ci'), unique=True)
    price = Column(Float, nullable=False)

    def __init__(self, dinnertype: str, price: float):
        self.dinnertype = dinnertype
        self.price = price


class Permission(Base):
    __tablename__ = 'permission'
    id = Column(Integer, primary_key=True)
    permission = Column(String(30, 'utf8_unicode_ci'), nullable=False, unique=True)

    user = relationship("User", primaryjoin='User.id_permission == Permission.id', back_populates="permission")

    def __init__(self, permission: str):
        self.permission = permission

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(60, 'utf8_unicode_ci'), nullable=False, unique=True)
    password = Column(Text(collation='utf8_unicode_ci'), nullable=False)
    name = Column(String(50, 'utf8_unicode_ci'))
    lastname = Column(String(100, 'utf8_unicode_ci'))
    id_permission = Column(ForeignKey('permission.id'), index=True)

    permission = relationship('Permission', primaryjoin='User.id_permission == Permission.id', backref='users')
    userlist = user = relationship("Userlist", primaryjoin='Userlist.id_user == User.id', back_populates="user")

    def __init__(self, email: str, password: str, name: str, lastname:str, permission : int):
        self.email = email
        self.password = password
        self.name = name
        self.lastname = lastname
        self.id_permission = permission


class Userlist(Base):
    __tablename__ = 'userlist'
    id = Column(Integer, primary_key=True)
    id_user = Column(ForeignKey('user.id'), index=True)
    id_dinnerset = Column(ForeignKey('dinnerset.id'), index=True)
    bought = Column(Integer, server_default=FetchedValue())

    dinnerset = relationship('Dinnerset', primaryjoin='Userlist.id_dinnerset == Dinnerset.id', backref='userlists')
    user = relationship('User', primaryjoin='Userlist.id_user == User.id', backref='userlists')

    def __init__(self, id_user, id_dinnerset, bought):
        self.id_user = id_user
        self.id_dinnerset = id_dinnerset
        self.bought= bought