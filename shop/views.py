from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from .models import Category, Product


class HomeView(View):
    def get(self, request, category_slug=None):
        category_page = None
        if category_slug is not None:
            category_page = get_object_or_404(Category, slug=category_slug)
            products = Product.objects.filter(category=category_page, available=True)
        else:
            products = Product.objects.all().filter(available=True)
        return render(request, 'shop/home.html', {'category': category_page, 'products': products})


class ProductView(View):
    def get(self, request, category_slug, product_slug):
        try:
            product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        except Exception as e:
            return e
        return render(request, 'shop/product.html', {'product': product})


class CartView(View):
    def get(self, request):
        return render(request, 'shop/cart.html')
