from rest_framework import status

from tests.base import BaseTestCase


class TestPost(BaseTestCase):
    def test_get_all_posts(self):
        response = self.client.get(self.ALL_POSTS_ENDPOINT)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_post(self):
        user = self.create_auth_user()
        data = {"user": user.id, "title": "Test title", "content": "Test content"}
        response = self.client.post(self.CREATE_POST_ENDPOINT, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("title", response.data)
        self.assertIn("content", response.data)

    def test_create_wrong_post(self):
        user = self.create_auth_user()
        data = {
            "user": user.id,
            "title": "Wrong test title that has more than 100 characters. This is more than 100 characters.\
                        Wrong test title that has more than 100 characters. This is more than 100 characters.",
            "content": "Test content",
        }
        response = self.client.post(self.CREATE_POST_ENDPOINT, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_detail(self):
        created_post = self.create_post()
        response = self.client.get(self.POST_DETAIL.format(created_post.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Test title")
        self.assertEqual(response.data["content"], "Test content")
