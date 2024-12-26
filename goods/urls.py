from django.urls import include, path
from goods import views

app_name='goods'

urlpatterns: list = [
    path('<slug:category_slug>/', views.catalog, name='index'),
    path('product/<slug:product_slug>/', views.product, name='product'),
   
]