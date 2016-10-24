from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.http import HttpResponse
from django.core.urlresolvers import reverse

# Create your views here.

def index(request):
    return render(request, 'product/index.html')

def products(request):
    pass

def categories(request):
    pass

def product(request):
    pass

def secret(request):
    pass