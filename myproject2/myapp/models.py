from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length = 20)
    description = models.TextField()
    price = models.DecimalField(max_digits = 5,decimal_places = 2)
    expire = models.DateTimeField()

    def __str__(self):
        return f'{self.id}_{self.name}'