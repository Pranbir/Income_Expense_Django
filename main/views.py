from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'main/header_footer.html')


def Dashboard(request):
    return render(request, 'main/Dashboard.html')


def header(request):
    return render(request, 'main/header_footer.html')

def Transaction(request):
    return render(request, 'main/Transaction.html')


def Incomes(request):
    return render(request, 'main/Incomes.html')


def Expenses(request):
    return render(request, 'main/Expenses.html')


def Accounts(request):
    return render(request, 'main/Accounts.html')



def Budgets(request):
    return render(request, 'main/Budgets.html')



def Income_Categories(request):
    return render(request, 'main/Income_Categories.html')


def Expense_Categories(request):
    return render(request, 'main/Expense_Categories.html')


def Income_Vs_Expense(request):
    return render(request, 'main/Income_Vs_Expense.html')



def Income_Calendar(request):
    return render(request, 'main/Income_Calendar.html')


def Expense_Calendar(request):
    return render(request, 'main/Expense_Calendar.html')


def Manage_Profile(request):
    return render(request, 'main/Manage_Profile.html')


def Logout(request):
    return render(request, 'main/Logout.html')
