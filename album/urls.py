from django.urls import path
from .import views

urlpatterns = [
    path('', views.AddAlbum.as_view(), name='album'),
    path('delete/<int:id>/', views.DeletePost.as_view(), name='album_delete'),
]
