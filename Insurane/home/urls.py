from django.urls import path
from home import views



urlpatterns = [
    path('', views.index, name='home'),
    path('prediction', views.prediction, name='prediction'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('success/', views.success, name='success'),
    path('singup', views.singup, name='singup'),
    path('login', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout')
    

   
]
