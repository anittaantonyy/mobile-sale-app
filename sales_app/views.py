from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from sales_app.forms import LoginRegistration, customer_form, seller_form, manager_form
from sales_app.models import Customer, Seller


# Create your views here.
def index(request):
    return render(request, "app.html")


def about(request):
    return render(request, "new.html")


def Login(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        print(username)
        password = request.POST.get('pass')
        print(password)
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect('admin_template')
            elif user.is_customer:
                return redirect('customer_template')
            elif user.is_seller:
                return redirect('seller_template')
            # else:
            #     messages.info(request,'InvalidCredentials')
    return render(request, "login.html")






def customer_add(request):
    form1 = LoginRegistration()
    form2 = customer_form()
    if request.method == 'POST':
        form1 = LoginRegistration(request.POST)
        form2 = customer_form(request.POST)

        if form1.is_valid() and form2.is_valid():
            a = form1.save(commit=False)
            a.is_customer = True
            a.save()
            user1 = form2.save(commit=False)
            user1.user = a
            user1.save()
            return redirect('Login')
    return render(request, 'registration.html', {'form1': form1, 'form2': form2})


def seller_add(request):
    form1 = LoginRegistration()
    form2 = seller_form()
    if request.method == 'POST':
        form1 = LoginRegistration(request.POST)
        form2 = seller_form(request.POST)

        if form1.is_valid() and form2.is_valid():
            a = form1.save(commit=False)
            a.is_seller = True
            a.save()
            user1 = form2.save(commit=False)
            user1.user = a
            user1.save()
            return redirect('Login')
    return render(request, 'seller_registration.html', {'form1': form1, 'form2': form2})


def manager_add(request):
    form1 = LoginRegistration()
    form2 = manager_form()
    if request.method == 'POST':
        form1 = LoginRegistration(request.POST)
        form2 = manager_form(request.POST)

        if form1.is_valid() and form2.is_valid():
            a = form1.save(commit=False)
            a.is_manager = True
            a.save()
            user1 = form2.save(commit=False)
            user1.user = a
            user1.save()
            return redirect('Login')
    return render(request, 'manager_registration.html', {'form1': form1, 'form2': form2})


@login_required(login_url='Login')
def admin_template(request):
    return render(request, "admin_template/admin_template.html")
@login_required(login_url='Login')
def customer_template(request):
    return render(request, "customer_template/customer_template.html")
@login_required(login_url='Login')
def seller_template(request):
    return render(request, "seller_template/seller_template.html")


@login_required(login_url='Login')
def view_customer(request):
    data = Customer.objects.all()
    return render(request, "new_customer.html", {'new': data})

@login_required(login_url='Login')
def view_seller(request):
    data = Seller.objects.all()
    return render(request, "new_seller.html", {'new': data})
@login_required(login_url='Login')
def delete_customer_data(request,id):
    data = Customer.objects.get(id=id)
    data.delete()
    return redirect("view_customer")
@login_required(login_url='Login')
def update_customer_data(request,id):
    data = Customer.objects.get(id=id)
    form = customer_form(instance=data)
    if request.method == 'POST':
        form = customer_form(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect("view_customer")
    return render(request,'update_customer_data.html',{'form':form})

@login_required(login_url='Login')
def delete_seller_data(request,id):
    data = Seller.objects.get(id=id)
    data.delete()
    return redirect("view_seller")
@login_required(login_url='Login')
def update_seller_data(request,id):
    data = Seller.objects.get(id=id)
    form = seller_form(instance=data)
    if request.method == 'POST':
        form = seller_form(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect("view_seller")
    return render(request,'update_seller_data.html',{'form':form})


def Logout(request):
    return redirect("Login")