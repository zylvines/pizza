from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('register/', register_page, name='register'),
    path('login/', login_page, name='login'),
    path('logout/', user_logout, name='logout'),
]

