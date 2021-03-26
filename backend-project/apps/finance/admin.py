from django.contrib import admin
from .models import Account, Transaction, Expense, Product, Category, Subcategory, Store
# Register your models here.
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Product)
admin.site.register(Store)
admin.site.register(Account)
admin.site.register(Transaction)
admin.site.register(Expense)



# admin.site.register(Purchase)