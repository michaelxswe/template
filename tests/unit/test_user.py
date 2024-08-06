from app.user.models import UserAccountCreate


def test_get(test_data: UserAccountCreate, client):
    response = client.get(url="/users/1")

    status_code = response.status_code

    assert status_code == 404
