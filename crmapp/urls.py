from django.urls import path
from .views import *

urlpatterns = [
    path('login/', loginView, name='login'),
    path('logout/', logoutView, name='logout'),
    path('register', registerView, name='register'),
    path('', homeView, name='home'),
    path('user_page/', userPageView, name='user_page'),
    path('accounts_settings/', accountSettingsView, name='accounts_settings'),
    path('create_customer/', createCustomerView, name='create_customer'),
    path('view_customer/<int:pk>/', customerDetailView, name='view_customer'),
    path('create_order/<str:pk>/', orderCreateView, name='create_order'),
    path('update_order/<str:pk>/', updateOrderView, name='update_order'),
    path('update_customer/<str:pk>/', customerUpdateView, name='update_customer'),
    path('delete_order/<str:pk>/', orderDeleteView, name='delete_order'),
    path('delete_order/<str:pk>/customer',
         orderDeleteInCustomerView, name='deleteorder_customer'),
    path('delete_customer/<str:pk>/', deleteCustomerView, name='delete_customer'),
    
    
   

]
