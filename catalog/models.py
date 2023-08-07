from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    name_product = models.CharField(max_length=100, verbose_name='название продукта')
    description = models.CharField(max_length=100, verbose_name='описание')
    image = models.ImageField(upload_to='products/', verbose_name='изображение', **NULLABLE)
    category = models.CharField(max_length=100, verbose_name='категория')
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='цена за покупку')  # Число с плавающей точкой (для денежных значений)
    date_creation = models.DateField(auto_now_add=True, verbose_name='дата создания')  # Автоматически устанавливается при создании
    date_modified = models.DateField(auto_now=True, verbose_name='дата изменения')  # Автоматически обновляется при каждом сохранении

    def __str__(self):
        return f'{self.name_product} {self.description}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('name_product',)




class Category(models.Model):
    name_product = models.CharField(max_length=30, verbose_name='название продукта')
    description = models.CharField(max_length=100, verbose_name='описание')


    def __str__(self):
        return f'{self.name_product} {self.description}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('name_product',)