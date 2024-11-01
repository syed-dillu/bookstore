import os
import sys
sys.path.append(os.getcwd())
import pytest
from sqlmodel import SQLModel
from bookstore.database import engine


@pytest.fixture(scope="session",autouse=True)
def setup_database():
    """

    Fixture to set up the database for testing.
    This fixture runs once per test session. It drops all existing tables, creates new tables,
    and provides a clean database state for tests. After all tests have run, it drops the tables again.

    """    
    SQLModel.metadata.drop_all(bind=engine)
    SQLModel.metadata.create_all(bind=engine)
    yield
    SQLModel.metadata.drop_all(bind=engine)