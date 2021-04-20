from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from .forms import ContactForm

def contact(request):
    user_contact = None
    
    # Comment posted
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():

            # Save the comment to the database
            user_contact.save()
            return HttpResponseRedirect('contact')
    else:
        contact_form = ContactForm()

    
    context = {
        'contact_form': contact_form
    }
    
    return render(request, 'pages/contact.html', context)
