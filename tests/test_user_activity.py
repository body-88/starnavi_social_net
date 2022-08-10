from rest_framework import status

from tests.base import BaseTestCase


class TestUserActions(BaseTestCase):
    def test_activity(self):
        self.create_auth_user()
        response = self.client.get(self.USER_ACTIVITY_ENDPOINT)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["username"], "username")
