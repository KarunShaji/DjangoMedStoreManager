from django.shortcuts import render, redirect
from .forms import CreateEmployee, LoginForm, CreateRecordForm, UpdateRecordForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import Record
from django.contrib import messages
from django.http import JsonResponse


def homepage(request):
    return render(request, 'proddetails/index.html')


# Register a User

def register(request):
    form = CreateEmployee()
    if request.method == "POST":
        form = CreateEmployee(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Account created succesfully")
            return redirect("login")
    
    context = {'form':form}
    return render(request, 'proddetails/register.html', context=context)


# Login a User

def my_login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')

    context = {'form':form}
    return render(request, 'proddetails/my-login.html', context=context)


# User Logout

def user_logout(request):
    auth.logout(request)
    messages.success(request,"Logout success!")
    return redirect("login")


# Dashboard

@login_required(login_url='login')
def dashboard(request):
    my_records = Record.objects.all()
    context = {'records': my_records}
    return render(request, 'proddetails/dashboard.html', context=context)


# Create Record

@login_required(login_url='login')
def create_record(request):
    form = CreateRecordForm()
    if request.method == 'POST':
        form = CreateRecordForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request,"Record created!")
            return redirect("dashboard")
    
    context = {'form':form}
    return render(request, 'proddetails/create-record.html', context=context)


# Update Record

@login_required(login_url='login')
def update_record(request, pk):
    record = Record.objects.get(id=pk)
    form = UpdateRecordForm(instance=record)
    if request.method == 'POST':
        form = UpdateRecordForm(request.POST, instance=record)
        if form.is_valid:
            form.save()
            messages.success(request,"Record updated!")
            return redirect("dashboard")
        
    context = {'form':form}
    return render(request, 'proddetails/update-record.html', context=context)


# Read / View  Single Record

@login_required(login_url='login')
def singular_record(request, pk):
    all_records = Record.objects.get(id=pk)

    context = {'record':all_records}
    return render(request, 'proddetails/view-record.html', context=context)


# Delete Record

@login_required(login_url='login')
def delete_record(request, pk):
    if request.method == 'POST':
        record = Record.objects.get(id=pk)
        record.delete()
        messages.success(request, "Record deleted successfully!") 
        my_records = Record.objects.all()
        context = {'records': my_records}
        return render(request, 'proddetails/dashboard.html', context=context) 
    else:
        return redirect('dashboard')

# Search

@login_required(login_url='login')
def search(request):
    if request.method == 'GET':
        query = request.GET.get('searchbar')
        result = Record.objects.all().filter(name__istartswith=query)
        return render(request, 'proddetails/search-result.html', {'result': result,'query':query})