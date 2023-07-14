from django.shortcuts import render
from .models import Product


# view 1 com requisição do tipo GET
def index(request):
    product = Product.objects.all()
    context = {
        'curso': 'Home teste',
        'product': product
    }
    return render(request, 'index.html', context)


# view 2 com requisição do tipo GET
def contact(request):
    return render(request, 'contact.html')


# view 3 com requisição do tipo GET
def getProductByID(request, id):
    prodFilter = Product.objects.get(id=id)
    prod = {
        'product': prodFilter
    }
    return render(request, 'product.html', prod)

