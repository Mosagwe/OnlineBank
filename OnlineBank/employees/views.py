from django.shortcuts import render

# Create your views here.
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib import messages

def homepage(request):
    return render(request,'employees/homepage.html')



def register(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("/profile")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request,"employees/register.html",{"form":form})

def sign_in(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("/profile")
    else:
        form = AuthenticationForm()
        return render(request, "employees/signin.html", {"form": form})

def logout_view(request):
    # Logout the user if he hits the logout submit button
    logout(request)
    return redirect("/login")