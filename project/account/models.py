from django.db import models
from django.contrib.auth.models import AbstractUser ,BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password
# Create your models here.
BRANCH_CHOICES=[
    ('قلب', 'قلب'),

]
class Country(models.Model):
    name=models.CharField(max_length=20)
    delivery_cost=models.FloatField(default=100.00)

    def __str__(self):
        return self.name
#
class City(models.Model):
    name=models.CharField(max_length=20)
    country=models.ForeignKey(Country,on_delete=models.CASCADE)
    delivery_cost=models.FloatField(default=100.00)
    branch= models.CharField(max_length=20,choices=BRANCH_CHOICES)

    def __str__(self):
        return self.name
#
class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN= 'ADMIN','Admin'
        PHARMACY='PHARMACY','Pharmacy'
        CUSTOMER='CUSTOMER','Customer'
    base_role=Role.ADMIN
    role = models.CharField(max_length=20,choices=Role.choices)
    phone_number = PhoneNumberField(blank=True)
    country=models.ForeignKey(Country,on_delete=models.CASCADE,blank=True,null=True)
    city=models.ForeignKey(City,on_delete=models.CASCADE,blank=True,null=True)
    address=models.TextField(max_length=200)

    def save(self,*args,**kwargs):
        if not self.pk:
            self.role=self.base_role
            return super().save(*args,**kwargs)
#
@receiver(post_save, sender=User)
def TokenCreate(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)
#
class Pharmacy_Manager(BaseUserManager):
    def get_queryset(self, *args,**kwargs):
        results=super().get_queryset(*args,**kwargs)
        return results.filter(role=User.Role.PHARMACY)
#
class Pharmacy(User):
    base_role=User.Role.PHARMACY
    objects=Pharmacy_Manager()
    class Meta:
        proxy=True
#
class Customer_Manager(BaseUserManager):
    def get_queryset(self, *args,**kwargs):

        results=super().get_queryset(*args,**kwargs)
        return results.filter(role=User.Role.PHARMACY)
#
class Customer(User):
    base_role=User.Role.CUSTOMER
    objects=Customer_Manager()
    class Meta:
        proxy=True

class Branch(models.Model):
    name=models.CharField(max_length=20,choices=BRANCH_CHOICES)
    staff = models.ForeignKey(Pharmacy, on_delete=models.CASCADE,related_name='pharmacy', null=True, default=None)
    whats_app = PhoneNumberField(blank=True)
    whats_app2 = PhoneNumberField(blank=True)

