from django.shortcuts import render
from .models import Category, Product, Review

def categories_view(request):
    categories = Category.objects.all()
    return render(request, "categories.html", {"categories": categories})

def products_view(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})

def reviews_view(request):
    reviews = Review.objects.all()
    return render(request, "reviews.html", {"reviews": reviews})
