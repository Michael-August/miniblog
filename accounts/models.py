from django.db import models
from django.contrib.auth.models import User


class Entry(models.Model):
    post_title = models.CharField(max_length=50)
    post_body = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Entries'
