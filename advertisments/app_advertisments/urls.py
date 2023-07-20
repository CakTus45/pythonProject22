from django.urls import path
from .views import index_2, test, test_2, top_sellers

urlpatterns = [
    path('', index_2, name='index'),
    path('test/', test, name='test'),
    path('test_2/',test_2, name='test_2'),
    path('top_sellers', top_sellers,name='top_sellers')
]