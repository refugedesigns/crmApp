from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('create_customer/', CreateCustomerView.as_view(), name='create_customer'),
    path('view_customer/<int:pk>/', CustomerDetailView.as_view(), name='view_customer'),
    path('create_order/<str:pk>/', orderCreateView, name='create_order'),
    path('update_order/<str:pk>/', updateOrderView, name='update_order'),
    path('update_customer/<str:pk>/', customerUpdateView, name='update_customer'),
    path('delete_order/<str:pk>/', orderDeleteView, name='delete_order'),
    path('delete_order/<str:pk>/customer',
         orderDeleteInCustomerView, name='deleteorder_customer'),
    path('delete_customer/<str:pk>/', deleteCustomerView, name='delete_customer'),
    
   

]
