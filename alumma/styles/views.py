from django.shortcuts import render
from .models import Style, Contact
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse

def homepage(request):
    return render(request, 'homepage.html')

def style(request):
    styles = Style.objects.all()
    return render(request, 'style.html', {'styles': styles})


def sendDataForCallBack(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        if name and phone:
            Contact.objects.create(name=name, phone=phone)
            return JsonResponse({'status': 'success'})
    return render(request, 'callbackpage.html')
