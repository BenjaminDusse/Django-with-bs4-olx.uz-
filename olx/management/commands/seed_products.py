from django.core.management.base import BaseCommand, CommandError
from olx.services import olx_products
from olx.models import Product

class Command(BaseCommand):
    help = 'This command creates products'

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",  default=2, type=int, help="How many products do you want to create?")

    def handle(self, *args, **options):
        number = options.get("number")

        olx_products.get_products(Product, number)
        
        self.stdout.write(self.style.SUCCESS(f"{number} products created!"))
