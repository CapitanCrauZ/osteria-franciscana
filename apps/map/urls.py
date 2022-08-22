from importlib.resources import path
from unicodedata import name


from django.urls import path
from .views import MapView, base

urlpatterns = [
    path('', MapView.as_view(), name='map'),
    path('', base, name='base')
]