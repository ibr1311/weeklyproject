from django.db import models
from account.models import MyUser


class Post(models.Model):
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=150, db_index=True)
    text = models.TextField(blank=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)

