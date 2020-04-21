import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from users.models import User
from rooms.models import Room, Amenity, Facility, HouseRule, RoomType, Photo


class Command(BaseCommand):

    help = "Seed rooms"

    def add_arguments(self, parser):
        parser.add_argument("--number", default=1)

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = User.objects.all()
        all_room_types = RoomType.objects.all()
        seeder.add_entity(
            Room,
            int(number),
            {
                "name": lambda x: seeder.faker.address(),
                "host": lambda x: random.choice(all_users),
                "room_type": lambda x: random.choice(all_room_types),
                "price": lambda x: random.randint(100, 500),
                "beds": lambda x: random.randint(0, 5),
                "guest": lambda x: random.randint(0, 4),
                "bedrooms": lambda x: random.randint(0, 5),
                "baths": lambda x: random.randint(0, 5),
            },
        )

        created_photos = seeder.execute()
        created_clean = flatten(list(created_photos.values()))
        amenities = Amenity.objects.all()
        facilities = Facility.objects.all()
        rules = HouseRule.objects.all()
        for pk in created_clean:
            room = Room.objects.get(pk=pk)
            for i in range(3, random.randint(10, 17)):
                Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    file_img=f"/room_photos/{random.randint(1,17)}.jpg",
                    room=room,
                )
            for a in amenities:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    room.amenities.add(a)
            for f in facilities:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    room.facilities.add(f)
            for r in rules:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    room.house_rules.add(r)

        self.stdout.write(self.style.SUCCESS(f"{number} rooms created"))
