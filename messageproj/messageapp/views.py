from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request , 'login/index.html')

def message (request):
    return render (request , 'message/index.html')