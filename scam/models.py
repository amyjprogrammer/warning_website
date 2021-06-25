from django.db import models

# Comment section
class CommentSection(models.Model):
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()
