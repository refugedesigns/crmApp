from django.urls import path
from .views import HomeView,CreateCustomerView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('create_customer/', CreateCustomerView.as_view(), name='create_customer')

]