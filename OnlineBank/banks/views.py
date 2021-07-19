from django.shortcuts import render,redirect
from . import forms
from . import models
from banks.models import Bank
from banks.forms import BankForm

# Create your views here.
def index(request):
    return render(request,'banks/index.html')

def create(request):
    if request.method=="POST":
        form=BankForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/banks')

    else:
        form=BankForm()
    return render(request,'banks/create.html',{'form':form})

