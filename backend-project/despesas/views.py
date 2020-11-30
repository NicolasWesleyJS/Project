from rest_framework import viewsets, generics
from despesas.models import FinanceUser, Expense
from .serializer import FinanceUserSerializer, ExpenseSerializer, ExpenseListUserSerializer

# This is the primary repository by principal worker!
# This is a second commentary by the primary repository by principal worker!

class FinanceUserViewSet(viewsets.ModelViewSet):
    """Exibir todos os usuários"""
    queryset = FinanceUser.objects.all()
    serializer_class = FinanceUserSerializer

class ExpenseViewSet(viewsets.ModelViewSet):
    """Exibir todas as despesas"""
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class ExpenseListUser(generics.ListAPIView):
    """Listando todas as despesas de um usuário"""
    def get_queryset(self):
        query_set = Expense.objects.filter(user_id=self.kwargs['pk'])
        return query_set
    
    serializer_class = ExpenseListUserSerializer