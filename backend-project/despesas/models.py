from django.db import models
from django.utils import timezone


class FinanceUser(models.Model):

    name = models.CharField(max_length=100)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    birthdate = models.DateField()

    def __str__(self):
        return self.name


class Expense(models.Model):
    Categories = (
        ('H','House'),
        ('T', 'Transportation'),
        ('F', 'Food and Drinks'),
        ('E', 'Education'),
        ('HC', 'Health care'),
        ('G', 'General costs'),
    )

    user = models.ForeignKey(FinanceUser, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    category = models.CharField(max_length=2, choices=Categories, blank=False, null=False, default='G')
    total = models.FloatField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.description
