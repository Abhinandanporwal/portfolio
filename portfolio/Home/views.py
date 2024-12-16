from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages
from Home.models import Contacts
import logging

logger = logging.getLogger(__name__)

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if len(name) <= 1 or len(name) >= 50:
            messages.error(request, 'Length of name should be greater than 2 and less than 50')
            return render(request, 'home.html')
        if len(email) <= 1 or len(email) >= 254:
            messages.error(request, 'Invalid email, try again')
            return render(request, 'home.html')
        if len(subject) <= 1 or len(subject) >= 250:
            messages.error(request, 'Length of subject should be greater than 2 and less than 250')
            return render(request, 'home.html')
        if len(message) <= 1 or len(message) >= 400:
            messages.error(request, 'Length of message should be greater than 2 and less than 400')
            return render(request, 'home.html')

        ins = Contacts(name=name , email=email , subject=subject , message=message)
        ins.save()
        messages.success(request, 'Thank you for contacting me. Your message has been saved.')
        return render(request, 'home.html')

    return render(request, 'home.html')

def home_view(request):
    return render(request, 'home.html')
