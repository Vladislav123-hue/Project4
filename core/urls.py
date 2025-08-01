from django.urls import path, include
#from shop import admin
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),  # подключаем urls приложения shop
]