from django.urls import path
from .views import whoamI

urlpatterns = [
    path('', whoamI),  
]