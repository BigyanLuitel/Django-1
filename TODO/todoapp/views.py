from django.shortcuts import render,redirect,get_object_or_404
from todoapp.models import Todo, User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request, 'todoapp/index.html')

login_required(login_url='login_page')
def todo_list(request):
    if request.method =='POST':
        title=request.POST.get('title')
        date=request.POST.get('date')
        user=request.user
        Todo.objects.create(
            title=title,
            date=date,
            user=user
        )
        messages.success(request, "Todo created successfully")
        
    todos=Todo.objects.filter(user=request.user)
    if request.GET.get('filter') == 'completed':
        todos = todos.filter(is_completed=True)
    
    context={
        'todos': todos,
        'page': 'todo_list'
    }
    return render(request,'todoapp/todo.html',context)
def update_todo(request, id):
    todo=get_object_or_404(Todo,id=id)
    if request.method=='POST':
        title=request.POST.get('title')
        date=request.POST.get('date')
        if todo.user != request.user:
            messages.error(request, "You do not have permission to update this todo")
            return redirect('todo_list')
        todo.title=title
        todo.date=date
        todo.save()
        messages.success(request, "Todo updated successfully")
        return redirect('todo_list')
    context = {
        'todo': todo,
        'page': 'update_todo'
    }
    return render(request, 'todoapp/update_todo.html', context)
def delete_todo(request, id):
    if request.method == "POST":
        data = get_object_or_404(Todo, id=id)
        if data.user != request.user:
            messages.error(request, "You do not have permission to delete this todo")
            return redirect('todo_list')
        data.delete()
    return redirect('todo_list')

def complete_todo(request, id):
    todo = get_object_or_404(Todo, id=id, user=request.user)
    todo.is_completed = True
    todo.save()
    return redirect('todo_list')
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

