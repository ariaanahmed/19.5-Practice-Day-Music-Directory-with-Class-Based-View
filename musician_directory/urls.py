from django.contrib import admin
from django.urls import path, include
from .import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home.as_view(), name='home'),
    path('album/', include('album.urls')),
    path('musician/', include('musician.urls')),
    path('', include('user_credintials.urls')),
    path('', include('user_credintials.urls')),
    path('edit/<int:id>/', views.EditPost.as_view(), name='EditPost'),
]
