#!/usr/bin/python3
"""
 add the State object
`Louisiana` to the db.
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

    lou_state = State(name='Louisiana')
    ses.add(lou_state)
    ses.commit()
    print('{0}'.format(lou_state.id))
    ses.close()
