from django.urls import path
from .views import MapView, base

urlpatterns = [
    path('', MapView.as_view(), name='mapping'),
    path('', base, name='base')
]