from django.urls import path

from .views import HomeView, ProductView, cart_detail, add_cart

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('category/<slug:category_slug>', HomeView.as_view(), name='products_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>', ProductView.as_view(), name='product_detail'),
    path('cart/', cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>', add_cart, name='add_cart'),
]
