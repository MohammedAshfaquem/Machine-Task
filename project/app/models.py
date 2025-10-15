from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()

    def _str_(self):
        return self.name


class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    date = models.DateField()

    def _str_(self):
        return self.product.name