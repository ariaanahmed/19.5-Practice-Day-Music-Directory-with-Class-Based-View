from django.urls import path
from .import views

urlpatterns = [
    path('', views.AddMusician.as_view(), name='musician')
]
