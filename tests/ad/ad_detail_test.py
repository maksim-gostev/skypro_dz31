import pytest

from tests.factories import AdFactory


@pytest.mark.django_db
def test_ad_detail(client,ad, hr_token):
    expected_response = {
        'id': ad.id,
        'author': ad.author.username,
            'category': ad.category.name,
        'name': ad.name,
            'price': ad.price,
        'is_published': ad.is_published,
            'description': None,
        'image': None,
        'location': []
    }

    response = client.get(f'/ad/{ad.id}/',content_type="application/json", HTTP_AUTHORIZATION="Bearer " + hr_token)

    assert response.status_code == 200
    assert response.data == expected_response





