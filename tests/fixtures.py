import pytest


@pytest.fixture
@pytest.mark.django_db
def hr_token(client, django_user_model, location):

    role = "member"
    age = 20
    username = "test1"
    password = "test"
    email = "test1@test.ru"
    birth_date = "1986-05-11"

    django_user_model.objects.create_user(
        role = role,
    age = age,
    username = username,
    password = password,
    email = email,
    birth_date = birth_date
    )
    response = client.post("/user/token/", {"username": username, "password": password},
                           content_type="application/json")
    return response.data["access"]

