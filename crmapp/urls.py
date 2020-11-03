from django.urls import path
from .views import HomeView,CreateCustomerView,CustomerDetailView, OrderUpdateView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('create_customer/', CreateCustomerView.as_view(), name='create_customer'),
    path('view_customer/<int:pk>/', CustomerDetailView.as_view(), name='view_customer'),
    path('update-order/<str:pk>/', OrderUpdateView.as_view(), name='update-order'),

]