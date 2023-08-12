from django.shortcuts import render, get_object_or_404
from .models import Product

def contacts_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        telephone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} {telephone} {message}')
    return render(request, 'catalog/contacts.html')


def home_page(request):
    products = Product.objects.all()  # Получаем все товары из базы данных
    return render(request, 'catalog/home.html', {'products': products})


def product_detail(request, product_id):
    # Извлекаем информацию о товаре из базы данных на основе его ID
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'catalog/product_detail.html', {'product': product})
