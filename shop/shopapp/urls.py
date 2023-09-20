from django.urls import path
from .views import categories_view, products_view, reviews_view

urlpatterns = [
    path("categories/", categories_view, name="categories"),
    path("products/", products_view, name="products"),
    path("reviews/", reviews_view, name="reviews"),
]
