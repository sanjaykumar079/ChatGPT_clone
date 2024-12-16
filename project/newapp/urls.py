from django.contrib import admin
from django.urls import path
from newapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login, name= 'login'),
    path('registration/', views.registration, name= 'registration'),
]