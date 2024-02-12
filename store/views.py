from django.shortcuts import render,get_object_or_404
from store.models import Product
from category.models import Category
from cart.views import _cart_id
from django.core.paginator import Paginator

def store(request, category_slug=None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        paginator = Paginator(products,1)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        p_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True).order_by('id')
        p_count = products.count()
        paginator = Paginator(products,3)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)

    context = {
        'products': paged_products,
        'p_count': p_count,
        'categories':categories,
    }
    return render(request, 'store/store.html', context)

def product_detail(request,category_slug,product_slug):
    try:
        single_product = Product.objects.get(category__slug = category_slug,slug = product_slug)
    except Exception as e:
        raise e
    context = {
        'single_product':single_product,
    }
    return render(request,'store/product_details.html',context)