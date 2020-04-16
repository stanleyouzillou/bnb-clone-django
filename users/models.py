from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):

    """ Custom User Model """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    LANGUAGE_FRENCH = "fr"
    LANGUAGE_ENGLISH = "en"

    LANGUAGE_CHOICES = ((LANGUAGE_FRENCH, "French"), (LANGUAGE_ENGLISH, "English"))

    CURRENCY_USD = "usd"
    CURRENCY_EUR = "eur"

    CURRENCY_CHOICES = ((CURRENCY_USD, "USD"), (CURRENCY_EUR, "EUR"))

    avatar = models.ImageField(blank=True)
    gender = models.CharField(
        max_length=10, choices=GENDER_CHOICES, blank=True, null=False
    )
    bio = models.TextField(default="", blank=True)
    birthdate = models.DateField(blank=True, null=True)
    language = models.CharField(blank=True, choices=LANGUAGE_CHOICES, max_length=50)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=3, blank=True)
    superhost = models.BooleanField(default=False, null=True)

