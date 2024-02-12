from django.shortcuts import render
from store.models import Product
from django.db.models import Q

def home(request):
    products = Product.objects.all()
    return render(request,'home.html',{'products':products})


def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by('-created_date').filter(Q(description__icontains = keyword)|
            Q(product_name__icontains = keyword))
            product_count = products.count()
    context = {
        'products':products,
        'p_count':product_count,
    }
    return render(request,'store/store.html',context)