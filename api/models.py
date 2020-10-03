from django.db import models
from django.utils import timezone
from string import ascii_lowercase, ascii_uppercase
import random


class Post(models.Model):
    # id = models.IntegerField(primary_key=True, null=False, blank=False, auto_created=True)
    B = 'Boast'
    R = 'Roast'
    CHOICES = ((B, 'Boast'), (R, 'Roast'))
    post_type = models.CharField(max_length=5, choices=CHOICES)
    content = models.CharField(max_length=280)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)
    total_votes = models.IntegerField(default=0)

    def __str__(self):
        return self.post_type

    def upvote(self):
        self.upvotes += 1
        self.total_votes += 1
        return self.upvotes

    def downvote(self):
        self.downvotes += 1
        self.total_votes -= 1
        return self.downvotes
