from django.shortcuts import render
from django.http import HttpResponse

# /account -> this function below
def index(request):
    return render(request, 'index.html')
