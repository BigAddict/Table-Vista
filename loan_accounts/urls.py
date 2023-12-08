from django.urls import path
from .views import LoanApplicationTemplateView, LoanRepaymentTemplateView

urlpatterns = [
    path("application/", LoanApplicationTemplateView.as_view(), name="application"),
    path("repayment/", LoanRepaymentTemplateView.as_view(), name="repayment")
]
