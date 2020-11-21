from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView,DetailView,UpdateView,DeleteView
from .models import Customer, Product, Order
from .forms import CreateCustomerForm, OrderUpdateForm, CustomerUpdateForm,CreateOrderForm, CreateUserForm, CustomerSettingsForm
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect, Http404
from django.forms import inlineformset_factory
from django import forms
from .filters import OrderFilter
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.models import Group
# Create your views here.
@unauthenticated_user
def loginView(request):
    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "username or password incorrect!")

    context = {}
    return render (request,'crmapp/login.html', context)

def logoutView(request):
    logout(request)
    return redirect('login')

@unauthenticated_user
def registerView(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='customer')
            user.groups.add(group)

            Customer.objects.create(user=user, email=user.email, name=user.username)
            
            messages.success(request, "Account was created for " + username )
            return redirect('login')
    context = {
        'form': form,
    }
    return render(request, 'crmapp/register.html', context)

@login_required(login_url='login')
@admin_only
def homeView(request):
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
    return render(request, 'crmapp/dashboard.html', context)




@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def userPageView(request):

    
    orders = request.user.customer.order_set.all()
    delivered = orders.filter(status='Delivered')
    pending = orders.filter(status='Pending')
    filters = OrderFilter(request.GET, queryset=orders)
        

    context = {

        'orders': orders,
        'filters': filters,
        'delivered': delivered,
        'pending': pending
    }
    return render(request, 'crmapp/user_page.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def accountSettingsView(request):
    user = request.user.customer
    form = CustomerSettingsForm(instance=user)
    
    if request.method == "POST":
        form = CustomerSettingsForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('accounts_settings')
    context = {
        'form': form
    }

    return render(request, 'crmapp/accounts_settings.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createCustomerView(request):
    form = CreateCustomerForm()

    if request.method == "POST":
        form = CreateCustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form,
    }
    return render(request, 'crmapp/create_customer.html',context)


@login_required(login_url='login')
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


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def customerDetailView(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    filters = OrderFilter(request.GET, queryset=orders)
    context = {
        'customer': customer,
        'orders': orders,
        'filters': filters
    }
    return render(request, 'crmapp/customer.html', context)


@login_required(login_url='login')
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


@login_required(login_url='login')
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

        form = CustomerUpdateForm()
    context = {
            'form': form
        }
    return render(request, 'crmapp/update_customer.html', context)


@login_required(login_url='login')
def orderDeleteView(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('home')
    context = {
        'order': order
    }
    return render(request, 'crmapp/delete_order_home.html', context)


@login_required(login_url='login')
def orderDeleteInCustomerView(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('view_customer', pk=order.customer.id)

    context = {
        'order': order,
    }
    return render(request, 'crmapp/delete_order_customer.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteCustomerView(request, pk):
    customer = Customer.objects.get(pk=pk)

    if request.method =="POST":
        customer.delete()
        return redirect('/')

    return render(request, 'crmapp/delete_customer.html', {'customer':customer})

