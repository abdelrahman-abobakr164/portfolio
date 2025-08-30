from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from .models import *
from .forms import ContactForm


def index(request):
    works = Work.objects.all()
    msg = ''
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            send_mail(
                subject='Protfolio Contact', 
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['abdelrahmanboda164@gmail.com'],
                fail_silently=False
                
            )
            msg += "Your Message have been Sent Successfully"
        else:
            msg += "Don't Mess"
    return render(request, 'index.html', {'works':works, 'msg':msg})

def detail(request, slug):
    work = get_object_or_404(Work, slug=slug)
    return render(request, 'details.html', {'work':work})