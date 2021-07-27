from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class member(models.Model):
    TAGS = (
        ('Red','Red tag'),
        ('Grey','Grey tag'),
        ('Purple','Purple tag'),
        ('Orange','Orange tag'),
    )
    DOMAIN = (
    	('Tech','Tech domain'),
    	('Marketing','Marketing domain'),
    	('Design','Design domain'),
    	('Human Resources','Human resources domain'),
    	)
    reg_no = models.CharField(primary_key=True,max_length=10)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=60,unique=True)
    mob_no = PhoneNumberField(unique=True)
    dept = models.CharField(max_length=60)
    tag = models.CharField(max_length=6,choices=TAGS)
    domain = models.CharField(max_length=20,choices=DOMAIN)
