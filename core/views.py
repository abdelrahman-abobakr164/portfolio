from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from .models import *
from .forms import ContactForm


def index(request):
    works = Work.objects.all()
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
            return JsonResponse({"success": True, "message": "Thanks i'll get back to you soon."})
        else:
            return JsonResponse({"success": False, "message": "Don't Mess"}, status=400)
    return render(request, 'index.html', {'works':works})

def detail(request, slug):
    work = get_object_or_404(Work, slug=slug)
    return render(request, 'details.html', {'work':work})