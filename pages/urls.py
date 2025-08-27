from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('page<int:number>/', views.page, name='page'),
]
