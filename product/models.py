from django.db import models


class Product(models.Model):
    title = models.CharField(max_length = 25)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(
        upload_to='image/%Y/%m/%d',
        blank=True
    )
    def __str__(self) -> str:
        return f"{self.title} {self.price}"
class Contact(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email =models.EmailField()
    message = models.TextField()
    def __str__(self):
        return f"{self.name} {self.phone}"
    
# Create your models here.
