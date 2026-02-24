from django.db import models
from django.contrib.auth.models import User



class BaseActivityModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )
    
    class Meta:
        abstract = True
        
        
        
        
class Customer(BaseActivityModel):
    
    """ A basic customer model to store all necessary customer information. """
    
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        related_name="customer",
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
        max_length=255
    )
    contact_number = models.CharField(
        max_length=15
    )
    # address = models.
    
    
    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"
    
    
    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.email
        super().save(*args, **kwargs)    
    
    
    def __str__(self):
        return self.username