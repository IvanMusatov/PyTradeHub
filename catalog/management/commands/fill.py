from django.core.management.base import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Заполнить базу данных данными'

    def handle(self, *args, **kwargs):
        # Очистка существующих данных из базы данных
        Category.objects.all().delete()
        Product.objects.all().delete()

        # Добавление данных в базу данных
        category1 = Category.objects.create(name_product='Категория 1', description='Описание категории 1')
        category2 = Category.objects.create(name_product='Категория 2', description='Описание категории 2')

        Product.objects.create(name_product='Товар 1', description='Описание товара 1',
                               category=category1, purchase_price=10.99)
        Product.objects.create(name_product='Товар 2', description='Описание товара 2',
                               category=category2, purchase_price=19.99)

        self.stdout.write(self.style.SUCCESS('База данных успешно заполнена.'))
