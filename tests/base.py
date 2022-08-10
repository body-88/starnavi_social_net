from django.test import TestCase
from rest_framework.test import APIClient

from posts.models.post import Post
from users.models.users import User


class BaseTestCase(TestCase):
    REGISTRATION_ENDPOINT = "/api/registration/"
    TOKEN_ENDPOINT = "/api/token/"
    ALL_POSTS_ENDPOINT = "/api/posts/"
    POST_DETAIL = "/api/posts/{}/"
    CREATE_POST_ENDPOINT = "/api/posts/create/"
    LIKE_ENDPOINT = "/api/posts/like/"
    LIKE_ANALITICS_ENDPOINT = "/api/posts/analitics/"
    USER_ACTIVITY_ENDPOINT = "/api/users/activity/"
    user_data = {
        "username": "test",
        "password": "test",
        "email": "test@gmail.com",
        "first_name": "test",
        "last_name": "test",
    }

    def setUp(self):
        self.client = APIClient()

        self.email = "user@example.com"
        self.username = "username"
        self.password = "password"
        self.wrong_username = "wrong_username"
        self.wrong_password = "wrong_password"
        self.user = User.objects.create_user(self.username, self.email, self.password)

        self.data = {"username": self.username, "password": self.password}
        self.wrong_data = {
            "username": self.wrong_username,
            "password": self.wrong_password,
        }
        self.title = "Test title"
        self.content = "Test content"
        self.author = self.user

    def create_auth_user(self):
        user = User.objects.get(username="username")
        self.client.force_authenticate(user)
        return user

    def create_post(self):
        post = Post.objects.create(
            title=self.title, content=self.content, author=self.author
        )
        return post

    def create_like_object(self):
        post = self.create_post()
        user = self.create_auth_user()
        data = {"user": user.id, "post": post.id}
        response = self.client.post(self.LIKE_ENDPOINT, data, format="json")
        return response
