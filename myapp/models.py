
from django.db import models
from autoslug import AutoSlugField
from tinymce.models import HTMLField
from rest_framework import serializers

# Create your models here.
class ContactForm(models.Model):
    ContactForm_name=models.CharField(max_length=122)
    ContactForm_email=models.EmailField(max_length=122)
    ContactForm_pnumber=models.IntegerField()
    ContactForm_message=models.TextField()


    def __str__(self):
        return self.ContactForm_name
    
class ContactFormSerialzer(serializers.ModelSerializer):
    class Meta:
        model=ContactForm
        fields="__all__"

class House(models.Model):
    House_title=models.CharField(max_length=122)
    House_des=HTMLField()
    House_image=models.FileField(upload_to="images/",max_length=250,null=True,default=None)

    House_slug=AutoSlugField(populate_from="House_title",unique=True,null=True,default=None)

def __str__(self):
    return self.House_title


class Signup(models.Model):
    username = models.CharField(max_length=122)
    fname = models.CharField(max_length=122)
    lname = models.CharField(max_length=122)
    email = models.EmailField()
    password = models.CharField(max_length=122)

def __str__(self):
    return self.fname








