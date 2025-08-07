from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name="homepage"),
    path('styles/', views.style, name="style"),
    path('callback/', views.sendDataForCallBack, name="callback"),
    path('thankyoupage/', views.thankYouView, name='thank_you'),
    path('ourPortfolio/', views.ShowPortfolio, name='portfolioWorkPage'),
    path('register/', views.register, name='registerPage'),
    path('thankYouRegisterPage/', views.thankYouRegisterPage, name='registerPageThanks'),
    path('profile/', views.profilePage, name='profile'),
    path('loginPage/', views.loginPage, name='login'),
    path('profile/messages/', views.messagesPage, name='profile_messages'),
    path('profile/messages/chatWith=<str:username>', views.ChatPage, name='profile_messages_chat')
]