from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse

from .models import Category, Product

# Create your views here.

def index(request):
    return render(request, 'product/index.html')


def products(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    product_lists = category.product_set.all()
    context = {
        'category': category,
        "product_list": product_lists,
    }
    return render(request, 'product/products.html', context)


def categories(request):
    category_list = Category.objects.all()
    context = {
        'category_list': category_list,
    }
    return render(request, 'product/categories.html', context)

def product(request):
    pass

def secret(request):
    pass