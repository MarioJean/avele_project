from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Blogpost

def index(request):
    blog = Blogpost.objects.order_by('-list_date').filter(is_published=True)
    
    paginator = Paginator(blog, 4)
    page = request.GET.get('page')
    paged_blog = paginator.get_page(page)
    
    context = {
        'blog': paged_blog
    }
    
    return render(request, 'blog/blog.html', context)
    
def blogpost(request, blogpost_id):
    return render(request, 'blog/blogpost.html')

def search(request):
    return render(request, 'blog/search.html')