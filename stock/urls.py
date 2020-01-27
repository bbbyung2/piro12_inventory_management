from django.urls import path
from . import views

app_name = 'stock'

urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('<int:pk>/', views.detail_list, name='detail_list'),
    path('new/', views.item_new, name='item_new'),
    path('comp/', views.comp_list, name='comp_list'),
    path('comp/<int:pk>/', views.detail_comp, name='detail_comp'),
    path('comp/new/', views.comp_new, name='comp_new'),
]