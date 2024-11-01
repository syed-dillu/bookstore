import os
import sys
sys.path.append(os.getcwd())
import pytest
from sqlmodel import SQLModel
from bookstore.database import engine

@pytest.fixture(scope="session",autouse=True)
def setup_database():
    """ Drop the data and create the data """
    SQLModel.metadata.drop_all(bind=engine)
    SQLModel.metadata.create_all(bind=engine)
    yield
    SQLModel.metadata.drop_all(bind=engine)