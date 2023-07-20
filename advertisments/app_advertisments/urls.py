from django.urls import path
from .views import index_2, test

urlpatterns = [
    path('', index_2),
    path('test/', test)
]