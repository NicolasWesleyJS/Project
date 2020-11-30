from rest_framework import serializers
from despesas.models import Expense, FinanceUser

class FinanceUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinanceUser
        fields = ['id', 'name', 'rg', 'cpf', 'birthdate']

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'        

class ExpenseListUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'