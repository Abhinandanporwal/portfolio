from django.db import models

class Contacts(models.Model):
    name= models.CharField(max_length=50)
    email= models.EmailField(max_length=254)
    subject= models.CharField(max_length=250)
    message= models.TextField(max_length=400)

