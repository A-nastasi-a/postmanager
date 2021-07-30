from django.shortcuts import render, redirect
from .models import Orders
from .forms import OrdersForm

# Create your views here.
def orders_home(request):
    orders = Orders.objects.order_by('-date_of_creating')
    return render(request, 'orders/orders_home.html', {'orders': orders})

def create(request):
    error = ''
    if request.method == 'POST':
        form = OrdersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'


    form = OrdersForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'orders/create.html', data)