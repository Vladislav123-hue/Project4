from django.shortcuts import redirect, render
from .models import Style, Contact, PortfolioWork, Profile, Chat
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import User
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


def ShowPortfolio(request):
    works = PortfolioWork.objects.all()
    return render(request, 'portfolioWorkPage.html', {'works': works})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST.get('username')
            return redirect(f'/thankYouRegisterPage?username={username}')
    else:
        form = UserCreationForm()
        
    return render(request, 'registerPage.html', {'form': form})

def thankYouRegisterPage(request):
     username = request.GET.get('username', '')
     return render(request, 'thankYouPageRegister.html', {'username': username})


@login_required(login_url="login")
def profilePage(request):
     
     user = request.user
     firstName = user.first_name
     secondName = user.last_name

     return render(request, 'ProfileLayout.html', {'firstName': firstName, 'lastName': secondName})


def loginPage(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            return redirect('profile')
    else:
        form = AuthenticationForm()
        
    return render(request, 'LoginPage.html', {'form': form})


def messagesPage(request):
    query = request.GET.get('q', '') 
    if query:
        users = User.objects.filter(username__icontains=query)
    else:
        users = []

    return render(request, 'messagesPage.html', {'users': users})

def ChatPage(request, username):
    senderModel = Profile.objects.get(user__username=request.user.username)
    receiverModel = Profile.objects.get(user__username=username)
    chatCollection = senderModel.chats.all()
    if request.method == 'POST':
        query = request.POST.get('chat', '')
        if query:
            newChatModel = Chat.objects.create(
                profile=senderModel,  
                sender = request.user.username,                     #создаю экземпляр модели
                receiver = username,
                content = query
            )       
            
            senderModel.chats.add(newChatModel)                                 # добавляю в экземпляр модели
            receiverModel.chats.add(newChatModel)
            chatCollection = senderModel.chats.all()                                # здесь хранится коллекция чатов  

    user = User.objects.get(username=username)
    first_name=user.first_name
    last_name=user.last_name

            
    
    return render(request, 'ChatPage.html', {'first_name': first_name, 'last_name': last_name, 'chatCollection' : chatCollection, 'username' : username, 'current_username': request.user.username})