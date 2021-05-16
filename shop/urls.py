from django.urls import path

from .views import HomeView, ProductView, cart_detail, add_cart, cart_remove, cart_delete, signUpView, loginView, \
    signOutView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('category/<slug:category_slug>', HomeView.as_view(), name='products_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>', ProductView.as_view(), name='product_detail'),
    path('cart/', cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>', add_cart, name='add_cart'),
    path('cart/remove/<int:product_id>', cart_remove, name='cart_remove'),
    path('cart/delete/<int:product_id>', cart_delete, name='cart_delete'),
    path('account/create/', signUpView, name='user_create'),
    path('account/login/', loginView, name='login'),
    path('account/signout/', signOutView, name='signout')
]
