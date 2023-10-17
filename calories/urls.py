from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('catalog/', views.catalog, name='catalog'),
    path('counter/', views.counter, name='counter'),
    path('history/', views.history, name='history'),
]
