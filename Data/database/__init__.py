from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from os import environ as ENV


ENV['dlogin'] = ENV.get('slogin') if 'slogin' in ENV else "sergiy1998"
ENV['dpaswd'] = ENV.get('spaswd') if 'spaswd' in ENV else "hspybxeR98>"
ENV['dbase'] = "dinnerplan"
ENV['dhost'] = "trashpanda.pwsz.nysa.pl"

class IConnector:
    def __init__(self):
        self._engines = create_engine('mysql://{login}:{password}@{host}/{databasename}?charset=utf8'.format(
            login=ENV["dlogin"],
            password=ENV["dpaswd"],
            host=ENV["dhost"],
            databasename=ENV["dbase"]
        ), pool_size=100, max_overflow=10)
        self.session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=self._engines))
        self.Base = declarative_base()
        self.Base.query = self.session.query_property()
        self.Base.metadata.create_all(bind=self._engines)

    def getSession(self):
        return self.session
    def getEngine(self):
        return self._engines
    def getBase(self):
        return self.Base

    def __del__(self):
        self.session.close()

"""
_engines = create_engine('mysql://{login}:{password}@{host}/{databasename}'.format(
    login = ENV["dlogin"],
    password = ENV["dpaswd"],
    host = ENV["dhost"],
    databasename = ENV["dbase"]
), pool_size=100, max_overflow=10)
session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=_engines))
Base = declarative_base()
Base.query = session.query_property()
Base.metadata.create_all(bind=_engines)
"""