from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.log_in, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('social-auth/', include('social_django.urls', namespace='social')),
]