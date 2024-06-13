from django.urls import path
from .import views

urlpatterns = [
    path('signup/', views.signup.as_view(), name='signup'),
    path('login/', views.user_login.as_view(), name='login'),
    path('logout/', views.user_logout.as_view(), name='logout'),
]