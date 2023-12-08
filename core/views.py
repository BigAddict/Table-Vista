from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from saving_accounts.models import SavingsAccount
from loan_accounts.models import LoanApplication

def dashboard(request):
    if request.user.is_authenticated:
        # Access user information
        data = {}
        data['user'] = request.user.username
        data['account'] = SavingsAccount.objects.get(member=request.user.username)
        try:
            data['loan'] = LoanApplication.objects.get(applicant=request.user)
        except LoanApplication.DoesNotExist:
            data['loan'] = {'loan_amount': 0}
        return render(request, "core\dashboard.html", {'data': data})
    else:
        # User is not logged in
        user = None
        return render(request, "core\index.html")    
