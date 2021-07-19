from django.urls import path
from . import views

app_name = "employees"   


urlpatterns = [
    path("", views.homepage, name="homepage"),    
    path("register", views.register, name="register"),
    path("login", views.sign_in, name="login"), 
    path("logout", views.logout_view, name="logout"),   
]