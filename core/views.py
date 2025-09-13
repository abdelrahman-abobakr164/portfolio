from django.shortcuts import render, get_object_or_404
from .models import *


def index(request):
    works = Work.objects.all()
    return render(request, 'index.html', {'works':works})

def detail(request, slug):
    work = get_object_or_404(Work, slug=slug)
    return render(request, 'details.html', {'work':work})