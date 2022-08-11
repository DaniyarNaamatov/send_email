from django.urls import path, include
from AmberReq import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sent/', views.send_email, name='send_email')

]