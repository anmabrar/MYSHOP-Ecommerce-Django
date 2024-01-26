import requests
from django.core.management.base import BaseCommand
from products.models import Category, Product
from django.utils.text import slugify


class Command(BaseCommand):
    def handle(self, *args, **options):
        print('Creating data...')
        response = requests.get('https://fakestoreapi.com/products').json()

        for product in response:
            category, _ = Category.objects.get_or_create(
                title=product['category'],
                slug=slugify(product['category']),
                featured=True
            )
            Product.objects.create(
                category=category,
                title=product['title'],
                slug=slugify(product['title']),
                price=product['price'],
                thumbnail=product['image'],
                description=product['description'],
            )
        print('insertion complete.')
