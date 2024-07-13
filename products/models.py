from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='nombre')
    description = models.TextField(max_length=300, verbose_name='description')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='precio')
    available = models.BooleanField(default=True, verbose_name='disponible')
    photo = models.ImageField(upload_to='logos', blank=True, null=True, verbose_name='foto')
    
    
    def __str__(self) -> str:
        return self.name