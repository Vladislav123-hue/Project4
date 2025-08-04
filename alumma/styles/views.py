from django.shortcuts import redirect, render
from .models import Style, Contact

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
            return redirect(f'/thankyoupage?name={name}&phone={phone}')
    return render(request, 'callbackpage.html')


def thankYouView(request):
    name = request.GET.get('name', '')
    phone = request.GET.get('phone', '')
    return render(request, 'thankyoupage.html', {'name': name, 'phone': phone})