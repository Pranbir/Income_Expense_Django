from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Dashboard', views.header, name='Dashboard'),
    path('header', views.header, name='header'),
    path('Transaction', views.Transaction, name='Transaction'),
    path('Incomes', views.Incomes, name='Incomes'),
    path('Expenses', views.Expenses, name='Expenses'),
    path('Accounts', views.Accounts, name='Accounts'),
    path('Budgets', views.Budgets, name='Budgets'),
    path('Income_Categories', views.Income_Categories, name='Income_Categories'),
    path('Expense_Categories', views.Expense_Categories, name='Expense_Categories'),
    path('Income_Vs_Expense', views.Income_Vs_Expense, name='Income_Vs_Expense'),
    path('Income_Calendar', views.Income_Calendar, name='Income_Calendar'),
    path('Expense_Calendar', views.Expense_Calendar, name='Expense_Calendar'),
    path('Manage_Profile', views.Manage_Profile, name='Manage_Profile'),
    path('Logout', views.Logout, name='Logout'),
]