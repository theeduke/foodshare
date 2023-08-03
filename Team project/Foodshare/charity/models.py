from django.db import models

# Create your models here.
class Donations(models.Model):
    """Model for  donations."""

    donor_name = models.CharField(max_length=255)
    donor_email = models.CharField(max_length=50, blank = True, null=True)
    donor_mobile = models.CharField(max_length=20)
    Donation_type = models.CharField(max_length=255, null=False)
    quantity = models.IntegerField(blank = True, null=True)
    request = models.TextField(blank = True, null=True)
    #expiry_date = models.DateField()
    accepted = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    #updated_at = models.DateTimeField(auto_now=True)
    
    category = models.ManyToManyField('Category', related_name='item')


    def __str__(self):
        return self.donor_name

    class Meta:
        ordering = ["-created_at"] 
    
    

    #def __str__(self):
        #"""String representation of the model."""
        #return f"{self.donor_name} {self.donor_mobile}  donated {self.quantity} {self.Donation_type}"



class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
     return self.name

