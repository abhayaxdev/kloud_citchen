from django.db import models
from django.contrib.auth. models import User

from customers.models import BaseActivityModel

class DeliveryRider(BaseActivityModel):
    
    """ This model will store basic delivery rider related information. """
    
    #code = models.CharField
    
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE,
        related_name="delivery_rider",
        null=True, 
        blank=True
    )
    first_name = models.CharField(
        max_length=50, 
        verbose_name="First Name"    
    )
    last_name = models.CharField(
        max_length=50, 
        verbose_name="Last Name"    
    )
    username = models.CharField(
        max_length=50,
        null=True, 
        blank=True
    )
    email = models.EmailField(
        max_length=255,
        null=True,
        blank=True
    )
    vehicle_number = models.CharField(
        unique=True,
        max_length=50,
        verbose_name="Number Plate"
    )
    vehicle_name = models.TextField(
        max_length=25,
        null=True,
        blank=True,
        verbose_name="Name of vehicle"
    )
    contact_number = models.CharField(
        max_length=15
    )

    
    class Meta:
        verbose_name = "Delivery Rider"
        verbose_name_plural = "Delivery Riders"
    
    
    def __str__(self):
        return f"{self.first_name}{ self.last_name}"
    
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
