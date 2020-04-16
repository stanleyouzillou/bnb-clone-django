from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.


class CustomUserAdmin(UserAdmin):
    """Custoler User Admin"""

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )


admin.site.register(models.User, CustomUserAdmin)