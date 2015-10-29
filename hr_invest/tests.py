from django.test import TestCase
from django.contrib.auth.models import User
from .models import Investor, Investment
from hr_warehouse.models import Warehouse
from hr_cash.models import CashLog

# Create your tests here.


class InvestTestCase(TestCase):

    def test_something(self):
        user = User.objects.create(username='test')
        investor = Investor.objects.create(name='test_investor')
        warehouse = Warehouse.objects.create(name='base', is_root=True)

        investment = Investment.objects.create(
            investor=investor,
            warehouse=warehouse,
            amount=1,
            type=Investment.TYPE_CASH,
            created_by=user
        )

        CashLog.objects.create(
            content_object=investment,
            warehouse=warehouse,
            amount=investment.amount
        )
