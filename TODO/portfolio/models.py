from django.db import models

# Create your models here.
class contact(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.EmailField(max_length=100)
    message=models.TextField()
    
    def __str__(self):
        return self.Name