from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns: list = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]