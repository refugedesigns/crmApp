from django import forms
from .models import Customer


class CreateCustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('name', 'email', 'phone',)

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Name...'
                    }
                ),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
        }