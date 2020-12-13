from django.shortcuts import render

def index(request):
    return render(request, 'blog/blog.html')
    
def blogpost(request):
    return render(request, 'blog/blogpost.html')

def search(request):
    return render(request, 'blog/search.html')