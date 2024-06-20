from django.contrib import admin
from django.urls import path

from sales_app import views, seller_view, customer_view, admin_view

urlpatterns = [
    path("",views.index,name="index"),
    path("about",views.about,name="about"),
    path("Login",views.Login,name="Login"),
    path("customer_add",views.customer_add,name="customer_add"),
    path("seller_add",views.seller_add,name="seller_add"),
    path("manager_add",views.manager_add,name="manager_add"),
    path("admin_template",views.admin_template,name="admin_template"),
    path("customer_template",views.customer_template,name="customer_template"),
    path("seller_template",views.seller_template,name="seller_template"),

    path("view_customer",views.view_customer,name="view_customer"),

    path("view_seller", views.view_seller, name="view_seller"),
    path("delete_customer_data/<int:id>/", views.delete_customer_data, name="delete_customer_data"),
    path("update_customer_data/<int:id>/", views.update_customer_data, name="update_customer_data"),
    path("delete_seller_data/<int:id>/", views.delete_seller_data, name="delete_seller_data"),
    path("update_seller_data/<int:id>/", views.update_seller_data, name="update_seller_data"),
    path("seller_view",seller_view.mobile_rentals, name="mobile_rentals"),
    path("view_mobile_rentals",seller_view.view_mobile_rentals, name="view_mobile_rentals"),
    path("update_mobile_rentals_data/<int:id>/", seller_view.update_mobile_rentals_data, name="update_mobile_rentals_data"),
    path("delete_mobile_rentals_data/<int:id>/", seller_view.delete_mobile_rentals_data, name="delete_mobile_rentals_data"),
    path("customer_view", customer_view.user_view_product, name="user_view_product"),
    path("admin_view", admin_view.admin_view_product, name="admin_view_product"),
    path("add_to_cart/<int:id>/", customer_view.add_to_cart, name="add_to_cart"),
    path("view_cart_product", customer_view.view_cart_product, name="view_cart_product"),
    path("buy_now/<int:id>/", customer_view.buy_now, name="buy_now"),
    path("ordered_product", customer_view.ordered_product, name="ordered_product"),
    path("view_orders", seller_view.view_orders, name="view_orders"),
    path("view_fullorderd_products", admin_view.view_fullorderd_products, name="view_fullorderd_products"),
    path("feedback", customer_view.feedback, name="feedback"),
    path("view_feedback", customer_view.view_feedback, name="view_feedback"),
    path("view_product_feedback", admin_view.view_product_feedback, name="view_product_feedback"),
    path("update_product_feedback/<int:id>/", admin_view.update_product_feedback, name="update_product_feedback"),
    path("notification_add", admin_view.notification_add , name="notification_add"),
    path("view_notification", admin_view.view_notification , name="view_notification"),
    path("delete_notification_data/<int:id>/", admin_view.delete_notification_data, name="delete_notification_data"),
    path("update_notification_data/<int:id>/", admin_view.update_notification_data, name="update_notification_data"),
    path("view_added_notification", customer_view.view_added_notification, name="view_added_notification"),
    path("Logout",views.Logout,name="Logout")
]
