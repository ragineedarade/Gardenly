from django.db import models
class savecontact(models.Model):
    
    name=models.CharField(max_length=10)
    email=models.EmailField(max_length=32)
    subject = models.CharField(max_length=40)
    message= models.TextField(max_length=50)
    def __str__(self):
        return self.name
class submitreview(models.Model):
        
     name=models.CharField(max_length=20)
     course=models.CharField(max_length=30)
     year=models.IntegerField(max_length=20)
     review=models.TextField(max_length=5)
     def __str__(self):
         return self.name
 
# Create your models here.
