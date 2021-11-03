from django.contrib.auth.models import AbstractUser
from django.db import models

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

# Create your models here.
class CustomUser(AbstractUser):
    """Extend user model for future"""

    email = models.EmailField("Email", unique=True)
    send_mail = models.BooleanField(default=True, verbose_name="Отправлять сообщения")
    avatar = models.ImageField(upload_to="users_avatar", blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    city = models.ForeignKey("scraping.City", help_text='Required. 150 characters or fewer. Letters, digits and '
                                        '@/./+/-/_ only.', blank=True, null=True, on_delete=models.SET_NULL)
    #language = models.ForeignKey("scraping.Language", null=True, blank=True, on_delete=models.SET_NULL)
    phone = models.BigIntegerField(blank=True, null=True, unique=True, verbose_name="Телефон для связи")
    gender = models.CharField(verbose_name="пол", max_length=1, choices=GENDER_CHOICES, blank=True)

    def __str__(self):
        return f"{self.username} "
