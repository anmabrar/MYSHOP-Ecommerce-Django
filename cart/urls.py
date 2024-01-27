from django.urls import path
from .views import AddToCart, CartItems, AddCoupon

urlpatterns = [
    path('add-to-cat/<int:product_id>/', AddToCart.as_view(), name='add-to-cat'),
    path('cart/', CartItems.as_view(), name='cart'),
    path('add-coupon/', AddCoupon.as_view(), name='add-coupon')
]