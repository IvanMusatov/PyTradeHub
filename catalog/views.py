from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from .models import Product, BlogPost
from django.views import View
from django.http import HttpResponseRedirect


class ContactsView(View):
    def get(self, request):
        return render(request, 'catalog/contacts.html')

    def post(self, request):
        name = request.POST.get('name')
        telephone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} {telephone} {message}')
        return render(request, 'catalog/contacts.html')


class HomeListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'


class BlogCreateView(CreateView):
    model = BlogPost
    fields = ['title', 'slug', 'content', 'preview', 'published']

    def get_success_url(self):
        return reverse('blogpost_list')


class BlogListView(ListView):
    model = BlogPost
    template_name = 'catalog/blogpost_list.html'
    context_object_name = 'posts'
    queryset = BlogPost.objects.filter(published=True)


class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'catalog/blogpost_detail.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        obj.views += 1
        obj.save()
        return obj


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    fields = ['title', 'slug', 'content', 'preview', 'published']

    def form_valid(self, form):
        response = super().form_valid(form)
        return HttpResponseRedirect(self.object.get_absolute_url())


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    success_url = reverse_lazy('blogpost_list')
