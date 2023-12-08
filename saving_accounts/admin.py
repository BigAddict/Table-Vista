from django.contrib import admin
from .models import *

admin.site.register(SavingsAccount)
admin.site.register(InterestRate)
admin.site.register(Transaction)