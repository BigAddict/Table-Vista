from django.db import models
from django.contrib.auth.models import User

class LoanProduct(models.Model):
    product_name = models.CharField(max_length=50, unique=True)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    max_loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    min_loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    max_loan_term = models.PositiveIntegerField()
    min_loan_term = models.PositiveIntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='Loan_Products/')

    def __str__(self) -> str:
        return self.product_name

class LoanApplication(models.Model):
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(LoanProduct, on_delete=models.CASCADE)
    application_date = models.DateField(auto_now_add=True)
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20)
    approval_date = models.DateField(null=True, blank=True)
    disbursement_date = models.DateField(null=True, blank=True)

class Repayment(models.Model):
    loan = models.ForeignKey(LoanApplication, on_delete=models.CASCADE)
    installment_number = models.PositiveIntegerField()
    due_date = models.DateField()
    installment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=20)
    last_payment_date = models.DateField(null=True, blank=True)
    late_fee = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

class Collateral(models.Model):
    loan = models.ForeignKey(LoanApplication, on_delete=models.CASCADE)
    identification_type = models.CharField(max_length=50)
    front_image = models.ImageField(upload_to='collateral_details/front')
    back_image = models.ImageField(upload_to='collateral_details/back')

class PaymentHistory(models.Model):
    loan = models.ForeignKey(Repayment, on_delete=models.CASCADE)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.payment_date