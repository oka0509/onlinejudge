from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Problem(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    constraints = models.TextField()
    inputformat = models.TextField()
    outputformat = models.TextField()
    sampleinput1 = models.TextField()
    sampleoutput1 = models.TextField()
    sampleinput2 = models.TextField()
    sampleoutput2 = models.TextField() 
    sampleinput3 = models.TextField()
    sampleoutput3 = models.TextField()
    testcases = models.TextField()
    def publish(self):
        self.save()

    def __str__(self):
        return self.title