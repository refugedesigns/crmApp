from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

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
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='crmapp/password_reset.html'), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='crmapp/password_reset_sent.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='crmapp/password_reset_form.html'),
         name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='crmapp/password_reset_complete.html'),
         name='reset_password_complete'),
    
   

]
