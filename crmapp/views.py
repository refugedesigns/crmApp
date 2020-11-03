from django.shortcuts import render
from django.views.generic import TemplateView, CreateView,DetailView,UpdateView
from .models import Customer, Product, Order
from .forms import CreateCustomerForm, OrderUpdateForm
from django.shortcuts import get_object_or_404


# Create your views here.
class HomeView(TemplateView):

    template_name = 'crmapp/dashboard.html'


    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        customers = Customer.objects.all()
        products = Product.objects.all()
        orders = Order.objects.all()[:5]
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
    success_url = '/'

class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'crmapp/customer.html'
    context_object_name = 'customer'


    def get_context_data(self, **kwargs):
        context = super(CustomerDetailView, self).get_context_data(**kwargs)
        orders = Order.objects.filter(customer=self.object)
        context['orders'] = orders
        products = Product.objects.filter(name=self.object)
        context['products'] = products
        return context

class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderUpdateForm
    template_name = 'crmapp/update-order.html'
    context_object_name = 'order'
    success_url = '/'

    def get_initial(self):
        initial = super(OrderUpdateView, self).get_initial()

        content = self.get_object()
        initial['customer'] = content.customer
        initial['product'] = content.product
        initial['status'] = content.status

        return initial

    def get_object(self, *args, **kwargs):
        product = get_object_or_404(Order, pk=self.kwargs['pk'])
        return product
