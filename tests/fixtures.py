import pytest


@pytest.fixture()
@pytest.mark.django_db
def hr_token(client, user):
    response = client.post("/users/token/", {"username": user.username, "password": user.password}, format='json')

    return response.data["access"]