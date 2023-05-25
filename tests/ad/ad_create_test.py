import pytest


@pytest.mark.django_db
def test_ad_create(client, user, category):
    expected_response = {
        "id": 1,
        "category": category.name,
        "author": user.username,
        "is_published": False,
        "price": 24000,
        "name": "Стол из слэба и эпоксидной смолы",
        "description": "Стол из слэба и эпоксидной смолы"
    }

    data = {
        "author": "test",
        "category": "test",
        "name": "Стол из слэба и эпоксидной смолы",
        "price": 24000,
        "is_published": False,
        "description": "Стол из слэба и эпоксидной смолы"
    }

    response = client.post('/ad/create/', data=data, content_type="application/json")

    assert response.status_code == 201
    assert response.data == expected_response
