from datetime import datetime
from django.conf import settings
from django.db import models


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = datetime.now()
        self.save()

    def __str__(self):
        return self.title
