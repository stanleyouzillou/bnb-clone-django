import random
from django.contrib.admin.utils import flatten
from django.core.management.base import BaseCommand
from django_seed import Seed
from users.models import User
from rooms.models import Room
from lists.models import List


class Command(BaseCommand):

    help = "Seed lists"

    def add_arguments(self, parser):
        parser.add_argument("--number", type=int, default=1)

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = User.objects.all()
        all_rooms = Room.objects.all()
        seeder.add_entity(
            List, number, {"user": lambda x: random.choice(all_users),},
        )

        created = seeder.execute()
        cleaned = flatten(list(created.values()))
        for pk in cleaned:
            list_model = List.objects.get(pk=pk)
            to_add = all_rooms[random.randint(1, 5) : random.randint(6, 30)]
            list_model.rooms.add(*to_add)
        self.stdout.write(self.style.SUCCESS(f"{number} list(s) created"))
