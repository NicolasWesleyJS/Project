from django.db import models
from datetime import datetime

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
    TRANSFER = 'TR'
    EXPENSE = 'EX'
    INCOME = 'IM'
    TRANSACTION_TYPE_CHOICES = (
        (TRANSFER, 'Transfer'),
        (EXPENSE, 'Expense'),
        (INCOME, 'Income')      
    )
    flag = models.CharField(max_length=2, choices=TRANSACTION_TYPE_CHOICES)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    location = models.CharField(max_length=25)
    description = models.TextField(max_length=50)
    datetime = models.DateTimeField(default=datetime.now, blank=True)
    total_value = models.FloatField(blank=False)

    def __str__(self):
        return self.description    

class Expense(models.Model):
    item = models.CharField(max_length=40)
    single_value = models.FloatField(blank=False)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)

    def __str__(self):
        return self.item