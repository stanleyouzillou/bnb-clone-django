import random
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from django_seed import Seed
from users.models import User
from reservations.models import Reservation
from rooms.models import Room


class Command(BaseCommand):

    help = "Seed reservations"

    def add_arguments(self, parser):
        parser.add_argument("--number", type=int, default=1)

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        guests = User.objects.all()
        rooms = Room.objects.all()
        seeder.add_entity(
            Reservation,
            number,
            {
                "room": lambda x: random.choice(rooms),
                "guest": lambda x: random.choice(guests),
                "check_in": lambda x: datetime.now(),
                "check_out": lambda x: datetime.now()
                + timedelta(days=random.randint(3, 25)),
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} reservation(s) created"))
