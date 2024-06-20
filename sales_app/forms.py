from django.contrib.auth.forms import UserCreationForm
from django import forms

from sales_app.models import Customer, Seller, Login_view, Manager, Mobile_Rentals, Cart, Buy_Now, Feedback, \
    Notification


class LoginRegistration(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label="password",widget=forms.PasswordInput)
    password2 = forms.CharField(label="confirm password", widget=forms.PasswordInput)

    class Meta:
        model = Login_view
        fields = ('username','password1','password2')


class customer_form(forms.ModelForm):
    class Meta:
        model =Customer
        fields = ('__all__')
        exclude = ('user','status1')

class seller_form(forms.ModelForm):
    class Meta:
        model =Seller
        fields = ('__all__')
        exclude = ('user', 'status2')

class manager_form(forms.ModelForm):
    class Meta:
        model =Manager
        fields = ('__all__')
        exclude = ('user', 'status')


class mobile_rentals_form(forms.ModelForm):
    class Meta:
        model =Mobile_Rentals
        fields = ('__all__')
        exclude = ('user', 'status4')

class cart_form(forms.ModelForm):
    class Meta:
        model =Cart
        fields = ('__all__')
        exclude = ('user', 'cart_status5')


class Buy_now_form(forms.ModelForm):
    class Meta:
        model =Buy_Now
        fields = ('__all__')
        exclude = ('user',)

class feedback_form(forms.ModelForm):
    class Meta:
        model =Feedback
        fields = ('feedback',)

class notification_form(forms.ModelForm):
    class Meta:
        model =Notification
        fields = ('__all__')

