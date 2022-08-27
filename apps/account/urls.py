from importlib.resources import path
from xml.etree.ElementInclude import include


from django.urls import path, include
from .views import log_in, log_out, register, profile

urlpatterns = [
    path('', log_in, name='login'),
    path('logout/', log_out, name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('social-auth/', include('social_django.urls', namespace='social')),
]