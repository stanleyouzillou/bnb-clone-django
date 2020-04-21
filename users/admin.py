from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.


class CustomUserAdmin(UserAdmin):
    """Custoler User Admin"""

    list_filter = UserAdmin.list_filter + ("superhost",)

    list_display = UserAdmin.list_display + ("superhost", "language", "currency",)

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
