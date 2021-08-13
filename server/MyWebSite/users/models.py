from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    """Extend user model for future"""
    MALE = "M"
    FEMALE = "W"
    OTHER = "O"
    TRANS = "T"

    GENDER_CHOICES = (
        (MALE, "Male"),
        (FEMALE, "Female"),
        (TRANS, "Transgender"),
        (OTHER, "Other")
    )
    avatar = models.ImageField(upload_to="users_avatar", blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    city = models.CharField(max_length=150, help_text='Required. 150 characters or fewer. Letters, digits and '
                                                      '@/./+/-/_ only.', blank=True, null=True)
    phone = models.BigIntegerField(blank=True, null=True, unique=True, verbose_name="Телефон для связи")
    gender = models.CharField(verbose_name="пол", max_length=1, choices=GENDER_CHOICES, blank=True)