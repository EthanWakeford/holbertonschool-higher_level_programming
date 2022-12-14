#!/usr/bin/python3
"""Start link class to table in database."""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        result = session.query(State.id, State.name).first()
        if result is None:
            print("Nothing")
        else:
            print(f"{result.id}: {result.name}")
