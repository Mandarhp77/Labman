from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registration/', views.registration, name='registration'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('registration', views.registration, name='registration'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
]