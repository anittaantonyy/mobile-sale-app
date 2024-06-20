from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from sales_app.forms import Buy_now_form, feedback_form
from sales_app.models import Mobile_Rentals, Cart, Customer, Feedback, Notification

@login_required(login_url='Login')
def user_view_product(request):
    data = Mobile_Rentals.objects.all()
    return render(request, "customer_template/user_view_product.html", {'new': data})
@login_required(login_url='Login')
def add_to_cart(request,id):
    data = Mobile_Rentals.objects.get(id=id)
    user = request.user
    user_data = Customer.objects.get(user=user)
    print(user_data)
    obj = Cart(user=user_data, product=data)
    obj.save()
    return redirect("view_cart_product")
@login_required(login_url='Login')
def view_cart_product(request):
    user = request.user
    data = Customer.objects.get(user=user)
    Cart_obj=Cart.objects.filter(user=data)
    return render(request, "customer_template/view_cart_product.html", {'new': Cart_obj})
@login_required(login_url='Login')
def buy_now(request,id):
    data = Cart.objects.get(id=id)
    buy_form = Buy_now_form()
    if request.method == 'POST':
        form = Buy_now_form(request.POST)
        print(form)
        if form.is_valid():
            data.cart_status5 = 1
            data.save()
            obj = form.save(commit=False)
            obj.user = data
            print(obj)
            obj.save()
            return redirect('view_cart_product')
    return render(request, "customer_template/buy_product.html", {'form': buy_form })

@login_required(login_url='Login')
def ordered_product(request):
    user = request.user
    data = Customer.objects.get(user=user)
    Cart_obj = Cart.objects.filter(user=data ,cart_status5 =1)
    return render(request, "customer_template/oredered_product.html", {'new': Cart_obj })

@login_required(login_url='Login')
def feedback(request):
    if request.method == 'POST':
        user = request.user
        customer_data = Customer.objects.get(user=user)
        form = feedback_form(request.POST)
        if form.is_valid():
           obj = form.save(commit=False)
           print(obj)
           obj.user = customer_data
           obj.save()
           return redirect('view_feedback')
    else:
        form = feedback_form()
    return render(request, 'customer_template/feedback.html', {'form': form})
@login_required(login_url='Login')
def view_feedback(request):
    user = request.user
    customer_data = Customer.objects.get(user=user)
    feedback_data = Feedback.objects.filter(user=customer_data)
    return render(request, 'customer_template/view_feedback.html', {'form': feedback_data})
@login_required(login_url='Login')
def view_added_notification(request):
    data = Notification.objects.all()
    return render(request, "customer_template/view_added_notification.html", {'new': data})








