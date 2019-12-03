from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'base.html')

def header(request):
    return render(request, 'main/header_footer.html')