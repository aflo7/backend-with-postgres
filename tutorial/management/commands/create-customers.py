# myapp/management/commands/create_customers.py

from django.core.management.base import BaseCommand
from ...quickstart.models import Customer
import random
import string

class Command(BaseCommand):
    help = 'Creates mock customers'

    def handle(self, *args, **kwargs):
        # Generate mock customers
        num_customers = 10  # Number of mock customers to create
        for _ in range(num_customers):
            name = ''.join(random.choices(string.ascii_letters, k=10))
            address = ''.join(random.choices(string.ascii_letters + string.digits, k=20))
            contact_info = ''.join(random.choices(string.digits, k=10))
            tax_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
            tax_rate = round(random.uniform(0, 10), 2)
            
            # Create and save the customer
            Customer.objects.create(
                name=name,
                address=address,
                contact_info=contact_info,
                tax_id=tax_id,
                tax_rate=tax_rate
            )

        self.stdout.write(self.style.SUCCESS(f'{num_customers} customers created successfully'))
