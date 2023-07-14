from django.db import models


class Product(models.Model):
    name = models.CharField('Nome', max_length=100)
    price = models.DecimalField('Preço', max_digits=8, decimal_places=2)
    quantity = models.IntegerField('Quantidade em estoque')

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField('Nome', max_length=100)
    surname = models.CharField('Sobrenome', max_length=100)
    email = models.EmailField('E-mail', max_length=100)

    def __str__(self):
        return self.name