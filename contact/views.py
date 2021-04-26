from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Contact

# Create your views here.
def contact(request):
    if request.method == 'POST':
        contact=Contact()
        name = request.POST['name']
        email = request.POST['email']
        inquiry = request.POST['inquiry']

        
        contact.name=name
        contact.email=email
        contact.inquiry=inquiry
        
        contact.save()
        messages.success(request, 'Your inquiry has been submitted')
    return render(request, 'pages/contact.html')
     
