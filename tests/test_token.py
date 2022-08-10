from rest_framework import status

from tests.base import BaseTestCase


class TestUserToken(BaseTestCase):
    def test_token_endpoint(self):
        response = self.client.post("/api/token/", self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)

    def test_token_endpoint_with_invalid_credentials(self):
        response = self.client.post("/api/token/", self.wrong_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(
            response.data["detail"],
            "No active account found with the given credentials",
        )
