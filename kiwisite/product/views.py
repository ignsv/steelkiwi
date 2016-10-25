from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.utils import timezone
import datetime

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


def product(request, category_slug, product_slug):
    category = get_object_or_404(Category, slug=category_slug)
    product = get_object_or_404(Product, slug=product_slug)
    context = {
        'product': product,
    }
    return render(request, 'product/product.html', context)


def secret(request):
    now = timezone.now()
    product_lists = Product.objects.filter(created_at__lte = now, created_at__gte = now - datetime.timedelta(days=1))
    #add Ukrainian timezone. Product model uses UTC. Ukraine time_zone = UTC+3 in summertime
    for product in product_lists:
        product.created_at += datetime.timedelta(hours=3)
        product.modified_at += datetime.timedelta(hours=3)
    context = {
        "product_list": product_lists,
    }
    return render(request, 'product/secret.html', context)