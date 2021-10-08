from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Blogpost
from .forms import NewCommentForm


def index(request):
    blog = Blogpost.objects.order_by('-list_date').filter(is_published=True)
    
    paginator = Paginator(blog, 4)
    page = request.GET.get('page')
    paged_blog = paginator.get_page(page)
    
    context = {
        'blog': paged_blog
    }
    
    return render(request, 'blog/blog.html', context)
    
def blogpost(request, pk, slug):
    blogpost = get_object_or_404(Blogpost, pk=pk, slug=slug)
    blog2 = Blogpost.objects.order_by('-list_date').filter(is_published=True)[:3]
    comments = blogpost.comments.filter(status=True)
    user_comment = None
    
    # Comment posted
    if request.method == 'POST':
        comment_form = NewCommentForm(request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            user_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            user_comment.post = blogpost
            # Save the comment to the database
            user_comment.save()
            messages.success(request, 'Your comment has been submitted')
            return HttpResponseRedirect('blogpost' + str(blogpost.pk))
            
    else:
        comment_form = NewCommentForm()

    
    context = {
        'blogpost': blogpost,
        'blog2': blog2,
        'comments': user_comment,
        'comments': comments,
        'comment_form': comment_form
    }
        
    return render(request, 'blog/blogpost.html', context)

def search(request):
    queryset_list = Blogpost.objects.order_by('-list_date')
    
    #Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)
    
        
    context = {
        'blog': queryset_list,
    }
        
    return render(request, 'blog/search.html', context)

