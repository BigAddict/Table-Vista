from django.db import models
from django.contrib.auth.models import User

class InterestRate(models.Model):
    name = models.CharField(max_length=50)
    rate = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()

    def __str__(self) -> str:
        return self.name

class SavingsAccount(models.Model):
    account_number = models.CharField(max_length=10, unique=True)
    member = models.ForeignKey(User, on_delete=models.CASCADE, to_field='username')
    account_balance = models.DecimalField(max_digits=10, decimal_places=2)
    opening_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20)
    interest_rate = models.ForeignKey(InterestRate, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return self.account_number

class Transaction(models.Model):
    account = models.ForeignKey(SavingsAccount, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=20)
    transaction_amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    def __str__(self) -> str:
        return self.transaction_type