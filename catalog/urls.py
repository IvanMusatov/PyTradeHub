from django.urls import path

from catalog.views import HomeListView, ProductDetailView, ContactsView, BlogDetailView, BlogListView, BlogCreateView, \
    BlogPostDeleteView, BlogPostUpdateView
from . import views

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('catalog/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('blogpost/<int:pk>/', BlogDetailView.as_view(), name='blogpost_detail'),
    path('blogpost_list/', BlogListView.as_view(), name='blogpost_list'),
    path('blogpost/create/', BlogCreateView.as_view(), name='blogpost_create'),
    path('blogpost/<int:pk>/update/', BlogPostUpdateView.as_view(), name='blogpost_update'),
    path('blogpost/<int:pk>/delete/', BlogPostDeleteView.as_view(), name='blogpost_delete'),
]
