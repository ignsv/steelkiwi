from django.conf.urls import url

from . import views

app_name = 'product'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^products/$', views.categories, name='categories'),
    url(r'^secret/$', views.secret, name='secret'),
    url(r'^products/(?P<category_slug>[\w-]+)/$', views.products, name='products'),
    url(r'^products/(?P<category_slug>[\w-]+)/(?P<product_slug>[\w-]+)/$', views.product, name='product'),
]