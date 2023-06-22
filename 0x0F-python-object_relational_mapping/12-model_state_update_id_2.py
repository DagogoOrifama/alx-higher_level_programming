#!/usr/bin/python3
"""
change the name of a State object
from the db.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Updates a State object on the db.
    """

    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    eng = create_engine(db_uri)
    Session = sessionmaker(bind=eng)

    ses = Session()

    ari_state = ses.query(State).filter(State.id == '2').first()
    ari_state.name = 'New Mexico'
    ses.commit()
    ses.close()
