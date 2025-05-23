from django.shortcuts import render,redirect
from todoapp.models import Todo, User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
login_required(login_url='login_page')
def home(request):
    return render(request, 'todoapp/index.html')

def signup(request):
    if request.method=='POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        
        if User.objects.filter(username=username).exists():
            messages.error(request,username+"already exists")
            return render(request,'todoapp/signup.html')
        else:
            user=User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                password=password
            )
            user.save()
            messages.success(request,"User created successfully")
            return redirect('login_page')
        
        
    return render(request,'todoapp/signup.html')

def login_page(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        if not User.objects.filter(username=username).exists():
            messages.error(request, "User does not exist")
            return render(request, 'todoapp/login.html')
        user=authenticate(username=username,password=password)
        if user is None:
            messages.error(request, "Invalid credentials")
            return redirect('login_page')
        else:
            login(request,user)
            #messages.success(request, "Login successful")
            return redirect('home')
        
    return render(request,'todoapp/login.html')

def logout_page(request):
    logout(request)
    return redirect('login_page')