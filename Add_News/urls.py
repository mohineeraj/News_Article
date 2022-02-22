from django.urls import path
from .views import index, refresh

urlpatterns = [
    path('', index, name='index'),
    path('refresh', refresh),   
]