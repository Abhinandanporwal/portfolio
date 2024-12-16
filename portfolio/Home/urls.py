from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home_view'),  # Add this line
    path('contact/', views.contact_view, name='contact_view'),
]
