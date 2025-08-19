from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('', views.all_users, name='all_users'),
    path('user/<int:id>/', views.user_detail, name='user'),
]
