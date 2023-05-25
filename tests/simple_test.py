def test_a(client):
    response = client.get("/")
    assert response.status_code == 200
