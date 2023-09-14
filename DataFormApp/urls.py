# urls.py (inside your app folder)
from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_contribution, name='create_contribution'),
    path('input-success/', views.input_success, name='input_success'),
    path('contribution-list/', views.contribution_list, name='contribution_list'),
]

