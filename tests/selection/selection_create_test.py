import pytest
@pytest.mark.django_db
def test_selection_creste(client, ad, user, hr_token):
    expected_response = {
        "id": 1,
        "name": "test",
        "ads": ad.name,
        "user": user.username
    }

    data = {
        "name": "test",
        "ads": 1,
        "user": 1,

    }

    response = client.post('/selection/create', data=data,
                           content_type="application/json")

    assert response.status_code == 201
    assert response.data == expected_response

    """
    ,  HTTP_AUTHORIZATION="Bearer " + hr_token
    """