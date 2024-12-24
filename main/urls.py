from django.urls import include, path
from app import views

app_name='main'

urlpatterns: list = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]