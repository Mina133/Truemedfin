from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    package = models.IntegerField()
    number_of_pieces = models.IntegerField()
    def price(self):
        if self.number_of_pieces == 0:  # Avoid division by zero
            return 0
        return self.package / self.number_of_pieces
    def __str__(self):
        return self.name
    
class List(models.Model):
    name = models.CharField(max_length=100)
    items = models.ManyToManyField(Item)

    def list_price(self):
        return sum([item.price for item in self.items.all()])
    
    def __str__(self):
        return self.name

