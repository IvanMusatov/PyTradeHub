from django.shortcuts import render


def contacts_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        telephone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} {telephone} {message}')
    return render(request, 'catalog/contacts.html')


def home_page(request):
    return render(request, 'catalog/home.html')
