from django.urls import path
from django.urls import path

from . import views

from django.contrib.auth.views import LoginView
from django.contrib.auth.views import logout_then_login

app_name = 'app_accounts'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('entrar/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('cadastrar/', views.register, name='register'),
    path('editar-usuario/', views.edit, name='edit'),
    path('editar-senha/', views.edit_password, name='edit_password'),
    #path('sair/', views.logout, name='logout'),
    
]