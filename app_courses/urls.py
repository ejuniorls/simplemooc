from django.urls import path

from . import views

app_name = 'app_courses'

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:slug>/', views.details, name='details'),
]