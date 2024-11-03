from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, "base.html")

def register(request):
    return render(request, "register.html")

@login_required(login_url="/login")
def profile(request):
    return render(request, "profile.html")

def login_page(request):
    return render(request, "login.html")




def save_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        fname = request.POST.get("fname")
        email = request.POST.get("email")

        if User.objects.filter(username = username).exists():
            context = {
            "msg":"User alredy exist"   
             }
            return render(request, "register.html", context)
        
        user = User.objects.create(username = username, first_name = fname, email = email)
        user.set_password(password)
        user.save()

        context = {
            "msg":"data saved"   
         }
    return render(request, "register.html", context)


def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # check user is exist or not
        if not User.objects.filter(username = username).exists():
            context = {
                'msg':"user does not exist"
            }
            return render(request, "login.html" , context)
        
        # use authenticate because password is in increpted format
        user = authenticate(username=username, password=password)

        if user is None:
            context = {
                'msg':"username and password is wrong"
            }
            return render(request, "login.html" , context)
        
        else:
            login(request, user)   # add user in session
            return redirect("/profile")
        

def logout_page(request):
    logout(request)    # remove session
    return redirect("/login")
    





