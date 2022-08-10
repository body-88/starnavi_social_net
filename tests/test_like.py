from rest_framework import status

from tests.base import BaseTestCase


class TestLikes(BaseTestCase):
    def test_create_like(self):
        created_post = self.create_post()
        user = self.create_auth_user()
        data = {"user": user.id, "post": created_post.id}
        response = self.client.post(self.LIKE_ENDPOINT, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["message"], "Post successfully liked")

    def test_create_unlike(self):
        created_post = self.create_post()
        user = self.create_auth_user()
        data = {"user": user.id, "post": created_post.id}
        response = self.client.post(self.LIKE_ENDPOINT, data, format="json")
        response = self.client.post(self.LIKE_ENDPOINT, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["message"], "Post successfully unliked")

    def test_like_analitics(self):
        self.create_auth_user()
        self.create_like_object()
        response = self.client.get(self.LIKE_ANALITICS_ENDPOINT, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["likes"], 1)
