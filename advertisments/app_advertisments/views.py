from django.shortcuts import render
from django.http import HttpResponse
from .models import Advertisements
def index_2(request_2):
    advertisements = Advertisements.objects.all()
    context = {"advertisements": advertisements}
    return render(request_2, "index.html", context)

# def index_2(request_2):
#     return render(request_2, "index.html")

def top_sellers(request_2):
    return render(request_2, "top-sellers.html")

def test(request_2):
    return render(request_2, "test.html")

def test_2(request_2):
    return render(request_2, "test_2.html")