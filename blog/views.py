from django.shortcuts import render
from .models import Blogpost

def index(request):
    blog = Blogpost.objects.all()
    
    context = {
        'blog': blog
    }
    
    return render(request, 'blog/blog.html', context)
    
def blogpost(request):
    return render(request, 'blog/blogpost.html')

def search(request):
    return render(request, 'blog/search.html')