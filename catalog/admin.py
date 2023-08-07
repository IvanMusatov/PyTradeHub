from django.contrib import admin

from catalog.models import Product, Category


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_product')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_product', 'purchase_price', 'category')
    list_filter = ('category',)
    search_fields = ('name_product', 'description')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
