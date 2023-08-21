# ctrl+shift+r for clearing cache in browser
from django.urls import path
from app.views import *
urlpatterns = [
    path("",index,name='index'),
    path('login/',login,name='login1'),
    path('register/',register,name='register1'),
    path('logout/',logout,name='logout1'),
]