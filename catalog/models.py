from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    name_product = models.CharField(max_length=100, verbose_name='название продукта')
    description = models.CharField(max_length=100, verbose_name='описание')
    image = models.ImageField(upload_to='products/', verbose_name='изображение', **NULLABLE)
    category = models.CharField(max_length=100, verbose_name='категория')
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2,
                                         verbose_name='цена за покупку')  # Число с плавающей точкой (для денежных значений)
    date_creation = models.DateField(auto_now_add=True,
                                     verbose_name='дата создания')  # Автоматически устанавливается при создании
    date_modified = models.DateField(auto_now=True,
                                     verbose_name='дата изменения')  # Автоматически обновляется при каждом сохранении

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


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=150)
    content = models.TextField()
    preview = models.ImageField(upload_to='blog_previews/', blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published = models.BooleanField(default=False)
    views = models.PositiveIntegerField(default=0)

    def get_absolute_url(self):
        return reverse('blogpost_detail', args=[str(self.id)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'публикации'
        ordering = ('title',)
