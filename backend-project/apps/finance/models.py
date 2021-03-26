from django.db import models
from datetime import datetime

class Category(models.Model):
    category_name = models.CharField(max_length=25)

    def __str__(self):
        return self.category_name

class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory_name = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.category} ---> {self.subcategory_name}'

class Product(models.Model):
    product_name = models.CharField(max_length=25)
    Subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name

class Store(models.Model):
    store_name = models.CharField(max_length=30)

    def __str__(self):
        return self.store_name


class Account(models.Model):
    BANK = 'BA'
    CREDITCARD = 'CC'
    WALLET = 'WA'
    ACCOUNT_TYPE_CHOICES = (
        (BANK, 'Bank'),
        (CREDITCARD, 'Credit Card'),
        (WALLET, 'Wallet')
    )
    name = models.CharField(max_length=25)
    type_of = models.CharField(choices=ACCOUNT_TYPE_CHOICES, default=WALLET, max_length=2)
    initial_value = models.FloatField(blank=False)
    current_value = models.FloatField(blank=False)
    
    def __str__(self):
        return self.name

class Transaction(models.Model):

    TRANSACTION_TYPE_CHOICES = (
        ('EX', 'Expense'),
        ('IN', 'Income')      
    )
    
    flag = models.CharField(max_length=2, choices=TRANSACTION_TYPE_CHOICES)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    location = models.ForeignKey(Store, on_delete=models.CASCADE)
    description = models.TextField(max_length=50, blank=True)
    datetime = models.DateTimeField(default=datetime.now, blank=True)
    total_value = models.FloatField(blank=False)

    def __str__(self):
        return f'{self.description} - {self.datetime}'    

class Expense(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_value = models.FloatField(blank=False)
    quantity = models.FloatField(blank=False)

    def __str__(self):
        return f' {self.product} = R$ {self.product_value}'