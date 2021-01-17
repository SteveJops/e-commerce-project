from django.urls import path

from .views import HomeView, ProductView, CartView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('category/<slug:category_slug>', HomeView.as_view(), name='products_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>', ProductView.as_view(), name='product_detail'),
    path('cart/', CartView.as_view(), name='cart'),
]
