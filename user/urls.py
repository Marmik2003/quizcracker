from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_end, name='login'),
    path('register/', views.registration_view, name='register'),
    path('logout/', views.logout_view, name='logout_view')
]