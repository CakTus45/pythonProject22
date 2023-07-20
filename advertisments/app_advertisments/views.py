from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index_2(request_2):
    return render(request_2, "index.html")

def top_sellers(request_2):
    return render(request_2, "top-sellers.html")

def test(request_2):
    return render(request_2, "test.html")

def test_2(request_2):
    return render(request_2, "test_2.html")