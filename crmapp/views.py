from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from .models import Customer, Product, Order
from .forms import CreateCustomerForm

# Create your views here.
class HomeView(TemplateView):
    template_name = 'crmapp/dashboard.html'
    context_object_name = 'object_list'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        customers = Customer.objects.all()
        products = Product.objects.all()
        orders = Order.objects.all()
        delivered = Order.objects.filter(status='Delivered')
        pending = Order.objects.filter(status='Pending')
        
        context = {
            'customers': customers,
            'products': products,
            'orders': orders,
            'delivered': delivered,
            'pending': pending,
        }
        return context


class CreateCustomerView(CreateView):
    model = Customer
    form_class = CreateCustomerForm
    template_name = 'crmapp/create_customer.html'
        