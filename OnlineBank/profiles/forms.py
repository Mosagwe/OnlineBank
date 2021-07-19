from django.db import models
from django import forms
from .models import Branch,AccountType,BankAccount


class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = "__all__"

class AccountTypeForm(forms.ModelForm):
    class Meta:
        model = AccountType
        fields = "__all__"

class BankAccountForm(forms.ModelForm):
    class Meta:
        model = BankAccount
        fields = ['bankAccountName','accountNo','branch_id','accounttype_id','emp_id','totalBalance']

class MakeDepositForm(forms.ModelForm):   
    class Meta:
        model = BankAccount
        fields = ['accounttype_id','emp_id','depositAmout']