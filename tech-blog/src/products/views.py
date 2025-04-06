from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from src.products.models import Product

def home_view(request):
    #itml = Product.objects.all()
    #print("Products in View:", itml)  # Debugging
    context = {
        "product_list": Product.objects.all(),
        "primes": [2,3,5,7]
    }
    return render(request, "home.html", context)

def contact_view(request):
    return render(request, "contact.html")
