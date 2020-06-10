from django.urls import path

from . import views

app_name = 'app_simplemooc'

urlpatterns = [
    path('', views.simplemooc, name='index'),
    path('contato/', views.contact, name='contact'),
]