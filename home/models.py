from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import User, auth 


# migration = create chage and store in a file 

# migrate = apply the pending changes make by migration 

# Create your models here.
class Contact(models.Model):
    name= models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    desc=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name
    



class Profiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone= models.CharField(max_length=20)
    vehicle= models.CharField(max_length=20)

    def __str__(self):
        return self.phone


   

    
        