from django.db import models

# Create your models here.
class Product(models.Model):
    GENDER = (
        ('M','M'), 
        ('F','F'),
    )
    id = models.IntegerField(primary_key=True)
    product=models.CharField(max_length=40)
    purchase=models.CharField(max_length=40)
    sale=models.CharField(max_length=10)
    qty=models.CharField(max_length=10)
    gender=models.CharField(max_length=1,null=True, choices=GENDER)
    note=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.product