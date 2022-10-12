from django.shortcuts import render

from orders.forms import OrderCreationForm
from orders.models import OrderItem
from cart.cart import Cart

# Create your views here.
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreationForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            cart.clear()
            # launch asynchronous task
            # order_created.delay(order.id)
            return render(request, 'orders/order/created.xhtml', {
                'order': order,
            })
