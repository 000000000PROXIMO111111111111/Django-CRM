from django.urls import path
from . import views

#STEP 2
urlpatterns = [
    path('', views.home, name='home'),
    #path('login/', views.login_user, name='login'), #With this we can create a seperate login page
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register')
    
]