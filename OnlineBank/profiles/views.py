from django.shortcuts import render,redirect
from . import forms
from . import models
from banks.models import Bank
from profiles.models import Branch,AccountType,BankAccount
from profiles.forms import BranchForm,AccountTypeForm,BankAccountForm,MakeDepositForm


# Create your views here.
def dashboard(request):
    return render(request,'profiles/dashboard.html')

def show_banks(request):
    banks=Bank.objects.all()
    return render(request,'profiles/banks_show.html',{'banks':banks})



# Create your views here.

def create_branch(request):
    if request.method=="POST":
        form=BranchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/profile')

    else:
        form=BranchForm()
    return render(request,'profiles/branch_create.html',{'form':form})

def show_branches(request):
    branches=Branch.objects.all()
    return render(request,'profiles/branches_show.html',{'branches':branches})

def create_accounttype(request):
    if request.method=="POST":
        form=AccountTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/profile')

    else:
        form=AccountTypeForm()
    return render(request,'profiles/accounts_create.html',{'form':form})

def show_accounts(request):
    accounts=AccountType.objects.all()
    return render(request,'profiles/accounts_show.html',{'accounts':accounts})



def create_bankaccount(request):
    if request.method=="POST":
        form=BankAccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/profile')

    else:
        form=BankAccountForm()
    return render(request,'profiles/bankaccount_create.html',{'form':form})

def show_bankaccounts(request):
    bankaccounts=BankAccount.objects.select_related('accounttype_id')
    return render(request,'profiles/bankaccount_show.html',{'bankaccounts':bankaccounts})

def makedeposit(request):
    
    if request.method=="POST":
        form=MakeDepositForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/profile')

    else:
        form=MakeDepositForm()
    return render(request,'profiles/makedeposit.html',{'form':form})