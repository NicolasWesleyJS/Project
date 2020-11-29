from django.contrib import admin
from despesas.models import FinanceUser, Expense

class FinanceUsers(admin.ModelAdmin):
    list_display = ('id', 'name', 'rg', 'cpf', 'birthdate')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 20

class Expenses(admin.ModelAdmin):
    list_display = ('id', 'user', 'description', 'category', 'total', 'date')
    list_display_links = ('id', 'description')
    search_fields = ('category',)


admin.site.register(FinanceUser, FinanceUsers)
admin.site.register(Expense, Expenses)
