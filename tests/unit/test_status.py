def test_get(client):
    response = client.get("/status")
    assert response.status_code == 200
