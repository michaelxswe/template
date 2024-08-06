from app.user.models import UserAccountCreate
from faker import Faker


def test_create(test_data: UserAccountCreate, client):
    json = {
        "username": test_data.username,
        "password": test_data.password,
        "email": test_data.email,
    }
    response = client.post(url="/users", json=json)

    status_code = response.status_code
    data = response.json()

    assert status_code == 200
    assert data["id"] == 1
    assert data["username"] == test_data.username
    assert data["password"] == test_data.password
    assert data["email"] == test_data.email
    assert data["status"] == 1
    assert "created_at" in data


def test_get_by_id(test_data: UserAccountCreate, client):
    response = client.get(url="/users/1")

    status_code = response.status_code
    data = response.json()

    assert status_code == 200
    assert data["id"] == 1
    assert data["username"] == test_data.username
    assert data["password"] == test_data.password
    assert data["email"] == test_data.email
    assert data["status"] == 1
    assert "created_at" in data


def test_update_by_id(test_data: UserAccountCreate, client):
    fake = Faker()
    password = fake.password()

    response = client.patch(url="/users/1", json={"password": password, "email": None})

    status_code = response.status_code
    data = response.json()

    assert status_code == 200
    assert data["id"] == 1
    assert data["username"] == test_data.username
    assert data["password"] == password
    assert data["email"] is None
    assert data["status"] == 1
    assert "created_at" in data


def test_delete_by_id(client):
    response = client.delete(url="/users/1")

    status_code = response.status_code
    data = response.json()

    assert status_code == 200
    assert data["id"] == 1
