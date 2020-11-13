from django.db import models

# Create your models here.

class Customer(models.Model):
    name    = models.CharField(max_length=200, null=True)
    phone   = models.CharField(max_length=200, null=True)
    email   = models.EmailField(max_length=200, null=True)
    date_created    = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Product(models.Model):
    name    = models.CharField(max_length=200)
    price   = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    description = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    options = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=options, null=True, max_length=200)

    def __str__(self):
        return f'Order by '+ ' ' + self.customer.name

    class Meta:
        ordering = ['-date_created']
