from django.urls import path

from catalog.views import home_page, contacts_page
from . import views

urlpatterns = [
    path('', home_page),
    path('contacts/', contacts_page),
    path('catalog/<int:product_id>/', views.product_detail, name='product_detail'),
]
