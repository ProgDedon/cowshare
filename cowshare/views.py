from django.shortcuts import render
from .models import Category, Product

# Create your views here.
def index(request):
    products = Product.objects.filter(available=True)[0:6]

    categories = Category.objects.all()

    return render(request, 'cowshare/index.html',{
        'categories': categories,
        'products': products,
    })
    
    return render(request, 'cowshare/index.html')

def products(request):
    context = {
        
    }
    return render(request, 'cowshare/products.html',context)
