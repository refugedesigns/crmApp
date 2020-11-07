from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView,DetailView,UpdateView
from .models import Customer, Product, Order
from .forms import CreateCustomerForm, OrderUpdateForm, CustomerUpdateForm,CreateOrderForm
from django.shortcuts import get_object_or_404
from django.urls import reverse



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

class OrderCreateView(CreateView):
    model = Order
    form_class = CreateOrderForm
    template_name = 'crmapp/create_order.html'
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

def updateOrderView(request, pk):
    order = Order.objects.get(id=pk)

    form = OrderUpdateForm(instance=order)
    if request.method == "POST":
        form = OrderUpdateForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form':form,
    }
    return render(request,'crmapp/update_order.html',context)

def customerUpdateView(request, pk):
    customer = Customer.objects.get(id=pk)

    form = CustomerUpdateForm(instance=customer)
    if request.method == "POST":
        form = CustomerUpdateForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('view_customer', pk=pk)
        else:
            form = CustomerUpdateForm(instance=customer)
    context = {
            'form': form
        }
    return render(request, 'crmapp/update_customer.html', context)



