from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView,DetailView,UpdateView,DeleteView
from .models import Customer, Product, Order
from .forms import CreateCustomerForm, OrderUpdateForm, CustomerUpdateForm,CreateOrderForm
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect, Http404
from django.forms import inlineformset_factory
from django import forms



# Create your views here.
class HomeView(TemplateView):

    template_name = 'crmapp/dashboard.html'


    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        customers = Customer.objects.all()
        products = Product.objects.all()
        orders = Order.objects.all()
        first_five = Order.objects.all()[:5]
        delivered = Order.objects.filter(status='Delivered')
        pending = Order.objects.filter(status='Pending')
        
        context = {
            'customers': customers,
            'products': products,
            'orders': orders,
            'delivered': delivered,
            'pending': pending,
            'first_five': first_five,
        }
        return context


class CreateCustomerView(CreateView):
    model = Customer
    form_class = CreateCustomerForm
    template_name = 'crmapp/create_customer.html'
    success_url = '/'


def orderCreateView(request, pk):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), widgets={
     'product': forms.Select(attrs={'class': 'form-control'}),
     'status': forms.Select(attrs={'class': 'form-control'}),
    })
    
    customer = Customer.objects.get(id=pk)
    #form = CreateOrderForm(initial={'customer': customer})
    formset = OrderFormSet(queryset=Order.objects.none(),instance=customer)
    if request.method == 'POST':
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('view_customer', pk=pk)
    context = {
        'formset': formset,
        'customer':customer
    }
    return render(request, 'crmapp/create_order.html', context)




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

def orderDeleteView(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('home')
    context = {
        'order': order
    }
    return render(request, 'crmapp/delete_order_home.html', context)


def orderDeleteInCustomerView(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('view_customer', pk=order.customer.id)

    context = {
        'order': order,
    }
    return render(request, 'crmapp/delete_order_customer.html', context)

def deleteCustomerView(request, pk):
    customer = Customer.objects.get(pk=pk)

    if request.method =="POST":
        customer.delete()
        return redirect('/')

    return render(request, 'crmapp/delete_customer.html', {'customer':customer})

