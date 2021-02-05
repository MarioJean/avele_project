from django.shortcuts import render
from blog.models import Blogpost

def index(request):
    blog = Blogpost.objects.order_by('-list_date').filter(is_published=True)[:3]
    
    context = {
        'blog': blog
    }
    
    return render(request, 'pages/index.html', context)

def store(request):
    return render(request, 'pages/store.html')

def contact(request):
    return render(request, 'pages/contact.html')