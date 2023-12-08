from decimal import Decimal
from typing import Any
from django.http import HttpRequest
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import SavingsAccount, Transaction
from django.views.generic import TemplateView

@method_decorator(login_required, name='dispatch')
class DepositTemplateView(TemplateView):

    template_name = 'saving_accounts/deposit.html'

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

    def post(self, request):
        # Data preparation
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.user.username
        email = request.POST['email']
        amount = request.POST['amount']
        description = request.POST['description']

        # Validation and algorithm logic
        current_account = get_object_or_404(SavingsAccount, member=username)
        current_account.account_balance = current_account.account_balance + Decimal(amount)
        current_account.save()
        messages.success(request, f"Dear {fname} {lname}, You have added Ksh.{amount} to your {current_account.account_number} account")
        transaction = Transaction.objects.create(account=current_account,
                           transaction_type="Deposit",
                           transaction_amount=amount,
                           description=description)
        try:
            transaction.save()
        except Exception as e:
            print(e)

        return redirect('/')

@method_decorator(login_required, name='dispatch')
class WithdrawTemplateView(TemplateView):

    template_name = 'saving_accounts/withdraw.html'

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
    
    def post(self, request):
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.user.username
        email = request.POST['email']
        amount = request.POST['amount']
        description = request.POST['description']

        # Validation and algorithm logic
        current_account = get_object_or_404(SavingsAccount, member=username)
        if current_account.account_balance >= Decimal(amount):
            current_account.account_balance = current_account.account_balance - Decimal(amount)
            current_account.save()
            messages.success(request, f"Dear {fname} {lname}, You have added Ksh.{amount} to your {current_account.account_number} account")
        elif current_account.account_balance < Decimal(amount):
            messages.error(request, f"Dear {fname} {lname}, You do not have enough money on {current_account.account_number} to make a Ksh.{current_account.account_balance} withdrawal")
            return redirect('/')
        else:
            messages.error(request, "An error occured, please try again after sometime")
        transaction = Transaction.objects.create(account=current_account,
                           transaction_type="Withdraw",
                           transaction_amount=amount,
                           description=description)
        try:
            transaction.save()
        except Exception as e:
            print(e)

        return redirect('/')