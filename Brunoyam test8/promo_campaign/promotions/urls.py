from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registration/', views.user_registration, name='registration'),
    path('login/', views.user_login, name='login'),
    path('campaign_statistics/', views.campaign_statistics, name='campaign_statistics'),
    path('user_dashboard/', views.user_dashboard, name='user_dashboard'),
]