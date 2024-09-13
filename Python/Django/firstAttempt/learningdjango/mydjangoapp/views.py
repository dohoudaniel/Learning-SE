from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_page(request):
    return render(request, 'index.html', {'name': 'Dohou Daniel Favour'})

def add(request):
    firstValue = request.POST['num1']
    secondValue = request.POST['num2']
    result = int(firstValue) + int(secondValue)
    return render(request, 'result.html', {'result': result})
