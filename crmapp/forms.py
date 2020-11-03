from django import forms
from .models import Customer, Order


class CreateCustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('name', 'email', 'phone',)

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