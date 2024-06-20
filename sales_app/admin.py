from django.contrib import admin

from sales_app import models
from sales_app.models import Customer, Seller

# Register your models here.
admin.site.register(models.Login_view)
admin.site.register(models.Customer)
admin.site.register(models.Seller)
admin.site.register(models.Manager)
admin.site.register(models.Mobile_Rentals)
admin.site.register(models.Cart)
admin.site.register(models.Buy_Now)


