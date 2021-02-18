from django.test import TestCase
from .models import Account
# Create your tests here.


class AccountModelTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        Account.objects.create(name = 'First Account', 
                               type_of = 'BA',
                               initial_value = 1000,
                               current_value = 1000)

    def test_name_content(self):
        account = Account.objects.get(id=1)
        expected_object_name = f'{account.name}'
        self.assertEquals(expected_object_name, 'First Account')

    def test_type_of_content(self):
        account = Account.objects.get(id=1)
        expected_object_type_of = f'{account.type_of}'
        self.assertEquals(expected_object_type_of, 'BA')

    def test_initial_value_content(self):
        account = Account.objects.get(id=1)
        expected_object_initial_value = f'{account.initial_value}'
        self.assertEquals(expected_object_initial_value, 1000)


                        
