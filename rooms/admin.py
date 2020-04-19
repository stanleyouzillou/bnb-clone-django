from django.contrib import admin
from django.utils.html import mark_safe
from . import models

# Register your models here.


class PhotoInline(admin.TabularInline):
    model = models.Photo


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room Admin Definition """

    inlines = (PhotoInline,)

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "city", "address", "price")},
        ),
        ("Times", {"fields": ("check_in", "check_out", "instant_book")},),
        ("Spaces", {"fields": ("amenities", "facilities", "house_rules")}),
        (
            "More About the Space",
            {
                "classes": ("collapse",),
                "fields": ("guest", "beds", "bedrooms", "baths"),
            },
        ),
        ("Last Details", {"fields": ("host",)}),
    )

    list_display = (
        "name",
        "country",
        "city",
        "guest",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
        "count_photos",
        "total_rating",
    )

    ordering = ("name", "price", "bedrooms")

    list_filter = (
        "instant_book",
        "host__superhost",
        "host__gender",
        "city",
    )

    filter_horizontal = (
        "amenities",
        "facilities",
        "house_rules",
    )

    def count_photos(self, obj):
        return obj.photos.count()

    def count_amenities(self, obj):
        return obj.amenities.count()

    raw_id_fields = ("host",)

    count_amenities.short_description = "Nb amenities"

    search_fields = ("city", "^host__username")


@admin.register(models.RoomType, models.Amenity, models.Facility, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.rooms.count()


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Photo Admin Definition """

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width ="150px" src ="{obj.file_img.url}" />')

    get_thumbnail.short_description = "Thumbnail"
