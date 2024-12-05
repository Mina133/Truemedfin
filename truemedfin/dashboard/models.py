from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    package = models.IntegerField()
    number_of_pieces = models.IntegerField()
    def price(self):
        if self.number_of_pieces == 0 or self.package == 0:
            return 0
        return self.package / self.number_of_pieces

    def __str__(self):
        return self.name
    
class List(models.Model):
    name = models.CharField(max_length=100)
    items = models.ManyToManyField(Item)

    def list_price(self):
        items = self.items.all()
        return sum([item.price() for item in items])
    
    def __str__(self):
        return self.name

