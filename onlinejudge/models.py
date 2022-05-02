from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Problem(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    time_limits = models.IntegerField(default=0)
    memory_limits = models.IntegerField(default=0)
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
    testinput1=models.TextField(null=True)
    testoutput1=models.TextField(null=True)
    testinput2=models.TextField(null=True)
    testoutput2=models.TextField(null=True)
    testinput3=models.TextField(null=True)
    testoutput3=models.TextField(null=True)
    testinput4=models.TextField(null=True)
    testoutput4=models.TextField(null=True)
    testinput5=models.TextField(null=True)
    testoutput5=models.TextField(null=True)   
    def publish(self):
        self.save()

    def __str__(self):
        return self.title
    def gettestcase(self):
        list = [[self.testinput1,self.testoutput1], [self.testinput2,self.testoutput2], [self.testinput3,self.testoutput3], [self.testinput4,self.testoutput4], [self.testinput5,self.testoutput5]]
        return list

class Submission(models.Model):
    title = models.CharField(max_length=200)
    language = models.CharField(max_length=200,default='python3')
    code = models.TextField()
    submitteddate = models.DateTimeField(default=timezone.now)
    result = models.CharField(max_length=200)
    def __str__(self):
        return self.title
