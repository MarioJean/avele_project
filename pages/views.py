from django.shortcuts import render

def index(request):
    return render(request, 'pages/index.html')

def store(request):
    return render(request, 'pages/store.html')

def contact(request):
    return render(request, 'pages/contact.html')