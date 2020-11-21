from django import forms
from .models import Customer, Order
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class CreateCustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('name', 'email', 'phone')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name...'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email...'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone...'}),
        }
    def __init__(self, *args, **kwargs):
        super(CreateCustomerForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = ""
        self.fields['email'].label = ""
        self.fields['phone'].label = ""

class CustomerUpdateForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('name', 'email', 'phone')
    
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name...'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email...'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone...'}),
        }
    def __init__(self, *args, **kwargs):
        super(CustomerUpdateForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = ""
        self.fields['email'].label = ""
        self.fields['phone'].label = ""

class OrderUpdateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('customer', 'product', 'status')

        widgets = {
            'customer': forms.Select(attrs={'class': 'form-control'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(OrderUpdateForm, self).__init__(*args, **kwargs)
        self.fields['customer'].label = ""
        self.fields['product'].label = ""
        self.fields['status'].label = ""

class CreateOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('customer', 'product', 'status')

        widgets = {
            'customer': forms.Select(attrs={'class': 'form-control'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super(CreateOrderForm, self).__init__(*args, **kwargs)
        self.fields['customer'].label = ""
        self.fields['product'].label = ""
        self.fields['status'].label = ""


class UserOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('product', 'status')

        widgets = {
            'product': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(UserOrderForm, self).__init__(*args, **kwargs)
        self.fields['product'].label = ""
        self.fields['status'].label = ""


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']       


class CustomerSettingsForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
