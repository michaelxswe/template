import os
from app.user.models import UserAccountCreate
from faker import Faker
from fastapi.testclient import TestClient
from pytest import fixture


@fixture(scope="session")
def set_env():
    os.environ["ENV"] = "test"
    os.environ["DB_URL"] = "postgresql+psycopg2://postgres:postgres@localhost:5433/postgres"
    yield


@fixture(scope="session")
def client(set_env):
    from app.main import app

    with TestClient(app) as client:
        yield client


@fixture(scope="session")
def test_data():
    fake = Faker()

    yield UserAccountCreate(username=fake.user_name(), password=fake.password(), email=fake.email())
