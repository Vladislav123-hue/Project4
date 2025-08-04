from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage),
    path('styles/', views.style, name="style"),
    path('callback/', views.sendDataForCallBack, name="callback"),
    path('thankyoupage/', views.thankYouView, name='thank_you'),
]