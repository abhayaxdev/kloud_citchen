from django.db import models
from django.contrib.auth. models import User

from customers.models import BaseActivityModel, Customer




# class Order(models.Model):
    
#     """This model will store all order related information."""
    
class DeliveryRider(BaseActivityModel):
    
    """This model will store basic delivery rider related information."""
    
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




class Delivery(BaseActivityModel):
    
    """This model tracks all deliveries that take place."""
    
    class DeliveryStatus(models.IntegerChoices):
        COMPLETED = 1, "Completed"
        CANCELLED = 2, "Cancelled"
        NO_SHOW = 3, "No Show"
    
    delivery_num = models.CharField(
        max_length=8,
        verbose_name="Delivery Number",
        null=True,
        blank=True
    ) 
    rider = models.ForeignKey(
        DeliveryRider,
        verbose_name="Delivery rider",
        on_delete=models.SET_NULL,
        related_name="deliverd_by"
    )
    customer = models.ForeignKey(
        Customer,
        on_delete=models.SET_NULL,
        related_name="delivered_to"
        
    )
    # order = models.OneToOneField(
    #     "Order",
    #     on_delete=models.CASCADE,
    #     related_name="order_to_deliver"
    # )
    delivery_status = models.IntegerField(
        verbose_name="Delivery Status",
        choices=DeliveryStatus.choices,
        null=True,
        blank=True
    )
    delivered_at = models.DateTimeField()
    
    
    class Meta:
        verbose_name = 'Delivery'
        verbose_name_plural = 'Deliveries'
        
    
    def __str__(self):
        return f"{self.delivery_num}"
    
    
    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)