from django.db import models
from banks.models import Bank
from django.contrib.auth.models import User

# Create your models here.

class Branch(models.Model):
    branchName = models.CharField("Branch name", max_length=255, blank = True, null = True)
    branchCode = models.CharField("Branch code", max_length=255, blank = True, null = True)
    bankid=models.ForeignKey(Bank,on_delete=models.CASCADE)

    class Meta:
        db_table='branches'

    def __str__(self):
        return self.branchName

class AccountType(models.Model):
    accountName=models.CharField("Account Name",max_length=255, blank = True, null = True)

    class Meta:
        db_table='account_types'

    def __str__(self):
        return self.accountName

class BankAccount(models.Model):
    bankAccountName=models.CharField("Customer Name",max_length=255, blank = True, null = True)
    accountNo=models.IntegerField("Account Number",blank=True,null=True)
    totalBalance=models.IntegerField("Balance",blank=True,null=True)
    depositAmout=models.IntegerField("Deposit Amount",blank=True,null=True)
    withrawalAmount=models.IntegerField(blank=True,null=True)
    overdraftLimit=models.IntegerField(blank=True,null=True)
    branch_id=models.ForeignKey(Branch,on_delete=models.CASCADE)
    accounttype_id=models.ForeignKey(AccountType,on_delete=models.CASCADE)
    emp_id=models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        db_table='bankaccounts'

    def __str__(self):
        return self.bankAccountName


    