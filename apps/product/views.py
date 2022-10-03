from django.shortcuts import render, redirect
from .models import Product, Category
from .forms import ProductForm

# Create your views here.

def add_product(request):
    list = Category.objects.all()
    form = None
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/product/')
    else:
        form = ProductForm()
    context = {
        'title': 'Add Product',
        'form': form,
        'list': list
    }
    return render(
        request,
        'product/add_product.html',
        context
    )

def list_product(request):
    products = Product.objects.all()
    list = Category.objects.all()
    context = {
        'title': 'List Product',
        'products': products,
        'list': list,
    }
    return render(
        request,
        'product/list_product.html',
        context
    )

def modify_product(request, id):
    product_received = Product.objects.get(pk=id)
    list = Category.objects.all()
    form = None
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product_received)
        if form.is_valid():
            form.save()
            return redirect('/product/')
    else:
        form = ProductForm(instance=product_received)
    context = {
        'title': 'Modify Product',
        'form': form,
        'list': list,
    }
    return render(
        request,
        'product/modify_product.html',
        context
    )

def delete_product(request, id):
    product_deleted = Product.objects.get(pk=id)
    product_deleted.delete()
    return redirect('/product/')