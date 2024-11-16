from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='home'),
    path('shop/', views.celestial_list, name='category_list'),
    path('shop/category/<slug:category_slug>/', views.celestial_list, name='category_list'),
    path('shop/<slug:detail_slug>/', views.detail, name='detail'),
]
