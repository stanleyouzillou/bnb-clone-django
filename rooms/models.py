from django.db import models
from django_countries.fields import CountryField
from core import models as core_models

# Create your models here.


class AbstractItems(core_models.TimeStampedModel):

    """ Abstract Items """

    name = models.CharField(max_length=80)

    class meta:
        abstract = True


class RoomType(AbstractItems):

    """ RoomType Object Definition """

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Room Type"
        ordering = ["name"]


class Amenity(AbstractItems):

    """ Amenity Object Definition """

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Amenities"


class Facility(AbstractItems):

    """ Facility Model Definition """

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItems):

    """ House Rule Model Definition """

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "House Rule"


class Photo(core_models.TimeStampedModel):

    """ Photo Model Definition """

    caption = models.CharField(max_length=80)
    file_img = models.ImageField(upload_to="room_photos")
    room = models.ForeignKey("Room", related_name="photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


class Room(core_models.TimeStampedModel):

    """ Model Def """

    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guest = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField(auto_now=False, auto_now_add=False)
    check_out = models.TimeField(auto_now=False, auto_now_add=False)
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(
        "users.User", related_name="rooms", on_delete=models.CASCADE
    )
    room_type = models.ForeignKey(
        "RoomType", related_name="room_types", on_delete=models.SET_NULL, null=True
    )
    amenities = models.ManyToManyField("Amenity", related_name="rooms", blank=True)
    facilities = models.ManyToManyField("Facility", related_name="rooms", blank=True)
    house_rules = models.ManyToManyField("HouseRule", related_name="rooms", blank=True)

    def save(self, *args, **kwargs):
        self.city = str.capitalize(self.city)
        super().save(*args, **kwargs)

    def total_rating(self):
        all_reviews = self.reviews.all()
        all_ratings = 0
        for review in all_reviews:
            all_ratings += review.rating_average()
        return all_ratings / len(all_reviews)

    def __str__(self):
        return self.name
