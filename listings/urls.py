from django.urls import path

from . import views

app_name = 'listings'

urlpatterns = [
    path('', views.index, name='listings'),
    path('<str:pk>/', views.listing, name='listing'),
    path('search/', views.search_param, name='search'),
]