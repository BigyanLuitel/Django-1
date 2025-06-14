from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Todo(models.Model):
    title=models.CharField(max_length=200)
    date=models.DateTimeField(auto_now_add=True)
    is_completed=models.BooleanField(default=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE)