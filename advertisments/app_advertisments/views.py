from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index_2(request_2):
    return render(request_2, "index.html")

def test(request_2):
    return render(request_2, "test.html")