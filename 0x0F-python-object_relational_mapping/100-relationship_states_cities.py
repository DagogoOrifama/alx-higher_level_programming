#!/usr/bin/python3
"""
This script prints all City objects
from the database `hbtn_0e_14_usa`.
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access to the database and get the cities
    from the database.
    """

    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    eng = create_engine(db_uri)
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)

    ses = Session()
    cal_state = State(name='California')
    sfr_city = City(name='San Francisco')
    cal_state.cities.append(sfr_city)

    ses.add(cal_state)
    ses.commit()
    ses.close()
