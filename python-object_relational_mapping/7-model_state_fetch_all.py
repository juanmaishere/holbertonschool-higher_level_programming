#!/usr/bin/python3
from sys import argv
from model_state import Base
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database = argv[3]
    
    query = "mysql+mysqldb://{}:{}@localhost/{}"
    engine = create_engine(query.format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)

    session = Session(engine)
    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
    session.close()