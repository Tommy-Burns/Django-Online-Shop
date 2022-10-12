from django.shortcuts import redirect, render
from django.urls import reverse
from .models import OrderItem
from .forms import OrderCreationForm
# from .tasks import order_created
from cart.cart import Cart


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
            # clear the cart
            cart.clear()
            # launch asynchronous task
            # order_created.delay(order.id)
            # set order in session
            request.session['order_id'] = order.id
            # redirect to payment page
            return redirect(reverse('payment:process'))
            # return render(request, 'orders/order/created.xhtml', {
            #     'order': order
            #     })
    else:
        form = OrderCreationForm()
    return render(request, 'orders/order/create.xhtml', {
        'cart': cart,
        'form': form
        })
