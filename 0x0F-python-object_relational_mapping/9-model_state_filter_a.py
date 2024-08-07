#!/usr/bin/python3
"""
List all state Object with the letter (a) from the database hbtn_0e_6_usa
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

    state_object_with_a = session.query(State).filter(
        State.name.ilike('%a%')).order_by(State.id).all()
    for state in state_object_with_a:
        print("{}: {}".format(state.id, state.name))
    session.close()
