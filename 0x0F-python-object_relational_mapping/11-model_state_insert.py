#!/usr/bin/python3
"""
Insert data into table
"""
import sys
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    new_item = session.query(State).filter(State.id == 2).first()

    if new_item:
        new_item.name = 'New Mexico'
        session.commit()
    session.close()
