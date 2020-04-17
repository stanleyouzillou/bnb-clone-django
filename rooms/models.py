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
    file_img = models.ImageField()
    room = models.ForeignKey("Room", on_delete=models.CASCADE)

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
    host = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room_type = models.ForeignKey("RoomType", on_delete=models.SET_NULL, null=True)
    amenities = models.ManyToManyField("Amenity", blank=True)
    facilities = models.ManyToManyField("Facility", blank=True)
    house_rules = models.ManyToManyField("HouseRule", blank=True)

    def __str__(self):
        return self.name
