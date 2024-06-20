from django.contrib.auth.decorators import login_required
from django.http import request
from django.shortcuts import redirect, render

from sales_app.forms import mobile_rentals_form
from sales_app.models import Mobile_Rentals, Customer, Cart

@login_required(login_url='Login')
def mobile_rentals(request):
    if request.method == 'POST':
        u = request.user
        print(u)
        form = mobile_rentals_form(request.POST,request.FILES)
        print(form)
        if form.is_valid():
            obj=form.save(commit=False)
            print(obj)
            obj.user=u
            obj.save()
            return redirect('view_mobile_rentals')
    else:
        form = mobile_rentals_form()
    return render(request, 'seller_template/view_mobile_rentals.html', {'form': form})
@login_required(login_url='Login')
def view_mobile_rentals(request):
    user = request.user
    data = Mobile_Rentals.objects.filter(user=user)

    return render(request, "new_mobile_rentals.html", {'new': data})
@login_required(login_url='Login')
def delete_mobile_rentals_data(request,id):
    data = Mobile_Rentals.objects.get(id=id)
    data.delete()
    return redirect("view_mobile_rentals")
@login_required(login_url='Login')
def update_mobile_rentals_data(request,id):
    data = Mobile_Rentals.objects.get(id=id)
    form = mobile_rentals_form(instance=data)
    if request.method == 'POST':
        form = mobile_rentals_form(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect("view_mobile_rentals")
    return render(request,'update_mobile_rentals_data.html',{'form':form})

@login_required(login_url='Login')
def view_orders(request):
    user = request.user
    Cart_obj = Cart.objects.filter(product__user=user,cart_status5 =1)
    return render(request, "seller_template/view_orders.html", {'new': Cart_obj })


