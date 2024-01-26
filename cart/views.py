from django.shortcuts import render
from .carts import Cart
from django.views import generic
from django.contrib import messages
from products.models import Product
from django.shortcuts import get_object_or_404, redirect


# Create your views here.


class AddToCart(generic.View):
    def post(self, *args, **kwargs):
        product = get_object_or_404(Product, id=kwargs.get('product_id'))
        cart = Cart(self.request)
        cart.update(product.id, 1)
        return redirect('cart')


class CartItems(generic.TemplateView):
    template_name = 'cart/cart.html'

    def get(self, request, *args, **kwargs):
        product_id = request.GET.get('product_id', None)
        quantity = request.GET.get('quantity', None)
        clear = request.GET.get('clear', False)
        cart = Cart(request)

        if product_id and quantity:
            product = get_object_or_404(Product, id=product_id)
            if int(quantity) > 0:
                if product.in_stock:
                    cart = Cart(request)
                    cart.update(int(product_id),int(quantity))
                    return redirect('cart')
                else:
                    messages.warning(request, "The product is not in stock")
                    return redirect('cart')
            else:
                cart.update(int(product_id), int(quantity))
                return redirect('cart')

        if clear:
            cart.clear()
            return redirect('cart')

        return super().get(request, *args, **kwargs)
