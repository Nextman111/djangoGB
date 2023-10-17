from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(blank=False)
    phone = models.CharField(max_length=12)
    adress = models.CharField(max_length=100, blank=False)
    date_reg = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'id: {self.pk}. {self.name}'

    def as_dict(self):
        return {
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'adress': self.adress,
            'date_reg': self.date_reg,
        }


class Product(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=1000, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    count = models.IntegerField(default=0)
    date_update = models.DateField(auto_now=True)

    # def __str__(self):
    #     return f'id: {self.pk}. {self.title}'


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    costing = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    date_create = models.DateField(auto_now=True)

    # def __str__(self):
    #     return f'id: {self.pk}. {self.costing}'
