from django.core.management.base import BaseCommand

from storageapp.models import Client


class Command(BaseCommand):
    help = "Create new client"

    def add_arguments(self, parser):
        parser.add_argument(
            'name',
            type=str,
            help='Client name',
        )
        parser.add_argument(
            "email",
            type=str,
            help="email",
        )
        parser.add_argument(
            "phone",
            type=str,
            help="Phone number",
        )
        parser.add_argument(
            "adress",
            type=str,
            help="Adress",
        )

    def handle(self, *args, **kwargs):
        client = Client(
            name=kwargs.get('name'),
            email=kwargs.get('email'),
            phone=kwargs.get('phone'),
            adress=kwargs.get('adress')
        )

        client.save()

        self.stdout.write(f'{client}')
