from django.urls import path
from .views import DepositTemplateView, WithdrawTemplateView

urlpatterns = [
    path('deposit', DepositTemplateView.as_view(), name="deposit"),
    path('withdraw', WithdrawTemplateView.as_view(), name='withdraw')
]