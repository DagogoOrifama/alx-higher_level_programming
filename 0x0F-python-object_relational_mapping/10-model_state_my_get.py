#!/usr/bin/python3
"""
print the State object id
with the name passed as argument
from the db.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access to the database and get a state
    from it.
    """

    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    eng = create_engine(db_uri)
    Session = sessionmaker(bind=eng)

    ses = Session()
    instance = ses.query(State).filter(State.name == argv[4]).first()

    if instance is None:
        print('Not found')
    else:
        print('{0}'.format(instance.id))
