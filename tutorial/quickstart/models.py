from django.db import models

# Create your models here.
class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=255)
    tax_id = models.CharField(max_length=20)
    tax_rate = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name