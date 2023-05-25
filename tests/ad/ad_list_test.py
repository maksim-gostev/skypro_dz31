import pytest

from ads.ad.serializers import AdSerializer
from tests.factories import AdFactory

@pytest.mark.django_db
def test_list_ads(client):
    ads = AdFactory.create_batch(10)

    response = client.get('/ad/')

    expected_response = {
        'count': 10,
        'next': None,
        'previous': None,
        'results': AdSerializer(ads, many=True).data
    }

    assert response.status_code == 200
    assert response.data == expected_response
