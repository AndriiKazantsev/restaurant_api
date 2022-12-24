import pytest
from rest_framework.test import APIClient


client = APIClient()


@pytest.mark.django_db
def test_register_user():
    payload = dict(
        first_name="John",
        last_name="Doe"
    )

    response = client.post('r^employee$', payload)

    data = response.data
    assert data["first_name"] == payload["first_name"]
