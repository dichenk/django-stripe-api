from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=250)

    description = models.CharField(max_length=1000)

    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
