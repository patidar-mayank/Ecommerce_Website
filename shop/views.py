from django.http import HttpResponse
from django.shortcuts import render
from .models import Products, Order
from django.core.paginator import Paginator


def index(request):
    product_objects = Products.objects.all()

    # Search code
    item_name = request.GET.get('item_name')
    if item_name and item_name.strip():  # Check if item_name is not empty
        product_objects = product_objects.filter(title__icontains=item_name)

    # Paginator code
    paginator = Paginator(product_objects.order_by('id'), 4)  # Order by 'id' or any other field you prefer
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)

    return render(request, 'shop/index.html', {'product_objects': product_objects})

def detail(request, id):
    product_object = Products.objects.get(id=id)
    return render(request, 'shop/detail.html', {'product_object': product_object})


def checkout(request):
    if request.method == "POST":
        items = request.POST.get('items', '')
        name = request.POST.get('name', "")
        email = request.POST.get('email', "")
        address = request.POST.get('address', "")
        city = request.POST.get('city', "")
        state = request.POST.get('state', "")
        zipcode = request.POST.get('zipcode', "")
        total = request.POST.get('total', "")

        # For debugging, print or log these values to ensure they are correct
        print(f"Items: {items}, Name: {name}, Email: {email}, Address: {address}, City: {city}, State: {state}, Zipcode: {zipcode}, Total: {total}")

        # Save the order to the database (this assumes you have a model named Order defined)
        order = Order(items=items, name=name, email=email, address=address, city=city, state=state, zipcode=zipcode, total=total)
        order.save()

        return HttpResponse('Order placed successfully!')
    
    return render(request, 'shop/checkout.html')