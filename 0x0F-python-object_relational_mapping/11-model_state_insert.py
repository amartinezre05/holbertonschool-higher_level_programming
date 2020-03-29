#!/usr/bin/python3
""" add an State """
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    Session.configure(bind=engine)
    session = Session()
    new_state = State(name="Lousiana")
    session.add(new_state)
    session.commit()
    state = session.query(State).filter(State.name == "Lousiana").\
            order_by(State.id).first()
    print(state.id)
