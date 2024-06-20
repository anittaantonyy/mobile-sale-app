from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from sales_app.forms import feedback_form, notification_form
from sales_app.models import Mobile_Rentals, Cart, Feedback, Notification


@login_required(login_url='Login')
def admin_view_product(request):
    data = Mobile_Rentals.objects.all()
    return render(request, "admin_template/admin_view_product.html", {'new': data})
@login_required(login_url='Login')
def view_fullorderd_products(request):
    Cart_obj = Cart.objects.filter( cart_status5=1)
    return render(request, "admin_template/total_ordered.html", {'new': Cart_obj})
@login_required(login_url='Login')
def view_product_feedback(request):
    feedback_data = Feedback.objects.all()
    return render(request, 'admin_template/view_product_feedback.html', {'form': feedback_data})
@login_required(login_url='Login')
def update_product_feedback(request,id):
    feedback_data = Feedback.objects.get(id=id)

    if request.method == 'POST':
        data = request.POST.get("reply")
        feedback_data.reply = data
        feedback_data.save()
        return redirect("view_product_feedback")
    return render(request,'admin_template/update_product_feedback.html',{'form':feedback_data})

@login_required(login_url='Login')
def notification_add(request):
    form = notification_form()
    if request.method == 'POST':
        obj = notification_form(request.POST)
        if obj.is_valid():
            obj.save()
            return redirect("view_notification")
    return render(request, 'admin_template/notification.html', {'form': form})
@login_required(login_url='Login')
def view_notification(request):
    data = Notification.objects.all()
    return render(request, "admin_template/view_notification.html", {'new': data})
@login_required(login_url='Login')
def delete_notification_data(request,id):
    data = Notification.objects.get(id=id)
    data.delete()
    return redirect("view_notification")

@login_required(login_url='Login')
def update_notification_data(request,id):
    data = Notification.objects.get(id=id)
    form = notification_form(instance=data)
    if request.method == 'POST':
        form = notification_form(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect("view_notification")
    return render(request,'admin_template/update_notification_data.html',{'form':form})
