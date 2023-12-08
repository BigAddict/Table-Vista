from django.contrib import admin
from .models import Collateral, LoanApplication, LoanProduct, PaymentHistory, Repayment

# Register your models here.
admin.site.register(LoanProduct)
admin.site.register(LoanApplication)
admin.site.register(PaymentHistory)
admin.site.register(Repayment)
admin.site.register(Collateral)