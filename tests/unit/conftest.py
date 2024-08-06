import os
from app.user.models import UserAccountCreate
from faker import Faker
from fastapi.testclient import TestClient
from pytest import fixture
from unittest import mock


@fixture(scope="session")
def set_env():
    os.environ["ENV"] = "test"
    os.environ["DB_URL"] = "postgresql+psycopg2://postgres:postgres@localhost:1234/postgres"
    yield

@fixture(scope="session")
def patch_repository():
    mock_repository = mock.Mock()
    mock_repository.get_by_id.return_value = None

    with mock.patch("app.user.repository", mock_repository):
        yield


@fixture(scope="session")
def client(set_env, patch_repository):
    from app.main import app

    yield TestClient(app)


@fixture(scope="session")
def test_data():
    fake = Faker()

    yield UserAccountCreate(username=fake.user_name(), password=fake.password(), email=fake.email())
