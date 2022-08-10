from django.db import models

from users.models.users import User

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def likes_count(self):
        return self.likes.all().count()

    def __str__(self):
        return f"{self.title} by {self.author} on {self.date_posted}"
