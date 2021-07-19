from django.urls import path
from . import views

app_name = "profiles"   


urlpatterns = [
    path("", views.dashboard, name="dashboard"),    
    path("/branch/create", views.create_branch, name="createbranch"),
    path("/branch", views.show_branches, name="showbranches"),
    path("/banks", views.show_banks, name="showbanks"),
    path("/account/create", views.create_accounttype, name="createaccount"),
    path("/account", views.show_accounts, name="showaccounts"),
    
    path("/bankaccount/create", views.create_bankaccount, name="createaccount"),
    path("/bankaccount", views.show_bankaccounts, name="showbankaccounts"),
    path("/bankaccount/deposit", views.makedeposit, name="makedeposit"),
    
]