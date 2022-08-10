from rest_framework import status

from tests.base import BaseTestCase


class TestRegistration(BaseTestCase):
    def test_registration_endpoint(self):
        data = self.user_data
        response = self.client.post(self.REGISTRATION_ENDPOINT, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            response.data["message"], "Registration successfully completed"
        )
