# import pytest
#
#
# @pytest.mark.django_db
# def test_ad_create(client):
#     expected_response = {
#         "id": 1,
#         "category": "Мебель и интерьер",
#         "author": "petr_bo",
#         "is_published": False,
#         "price": 24000,
#         "name": "Стол из слэба и эпоксидной смолы",
#         "description": "Стол из слэба и эпоксидной смолы"
#     }
#
#     data = {
#         "id": 1,
#         "author": "petr_bo",
#         "category": "Мебель и интерьер",
#         "location": [
#             "Москва, м. Библиотека имени Ленина"
#         ],
#         "name": "Стол из слэба и эпоксидной смолы",
#         "price": 24000,
#         "is_published": False,
#         "description": "Стол из слэба и эпоксидной смолы"
#     }
#
#     response = client.post('/ad/create/', data=data, content_type="application/json")
#
#     assert response.status_code == 201
#     assert response.data == expected_response
