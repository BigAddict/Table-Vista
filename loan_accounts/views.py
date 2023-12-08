from django import http
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .models import LoanApplication, Repayment, Collateral, PaymentHistory
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from saving_accounts.models import SavingsAccount
from django.views.generic import TemplateView
from django.http import HttpRequest
from typing import Any

@method_decorator(login_required, name='dispatch')
class LoanApplicationTemplateView(TemplateView):
    template_name = 'loan_accounts/loan_application.html'

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        self.user = request.user
        return super().get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        data = {}
        data['user'] = self.user.username
        data['account'] = SavingsAccount.objects.get(member=self.user.username)
        context['data'] = data
        return context

@method_decorator(login_required, name='dispatch')
class LoanRepaymentTemplateView(TemplateView):
    template_name = 'loan_accounts/loan_repayment.html'

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        self.user = request.user
        return super().get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        data = {}
        data['user'] = self.user.username
        data['account'] = SavingsAccount.objects.get(member=self.user.username)
        context['data'] = data
        return context

@method_decorator(login_required, name='dispatch')
class LoanTemplateView(TemplateView):
    pass