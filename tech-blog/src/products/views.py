from django.shortcuts import render
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


#HttpResponse("""
        #<h1>Contact Page</h1><br><br>
        #<h2>This is Soumalya's Django app's Contact Page</h2>
        #<h4>Contacts:</h4>
        #<h4><a href="https://github.com/pro-grammer-SD">GitHub</a></h4>
    #""")