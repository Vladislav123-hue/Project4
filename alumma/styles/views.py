from django.shortcuts import render
from .models import Style

def homepage(request):
    return render(request, 'homepage.html')

def style(request):
    styles = Style.objects.all()
    return render(request, 'style.html', {'styles': styles})