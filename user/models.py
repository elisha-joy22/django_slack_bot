from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255)
    slack_id = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    image = models.CharField(max_length=400)

    def __str__(self):
        return self.name
    
    